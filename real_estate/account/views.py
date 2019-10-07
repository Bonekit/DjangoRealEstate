from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from contact.models import Contact


def user_login(request):
    title = 'User Login'
    template_name = 'account/login.html'
    form = LoginForm()
    context = {
        'title': title,
        'login_form': form,

    }

    # If the user is logged in
    if request.user.is_active:
        messages.error(request, "You are already logged in")
        return redirect('main:main-index')

    # Login
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('account:dashboard')
        else:
            messages.error(request, "Login was not successfull")
            form = LoginForm()
            return render(request, template_name, {'title': title, 'login_form': form})

    return render(request, template_name, context)


def register(request):
    title = 'Register | New User'
    template_name = 'account/register.html'

    # If the user is logged in
    if request.user.is_active:
        messages.error(request, "You are already logged in")
        return redirect('main:main-index')

    # Register
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        context = {
            'title': title,
            'registration_form': form,
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successfully")
            return redirect('main:main-index')
        else:
            messages.error(
                request, "Registration was not successfull")
            return render(request, template_name, context)

    # If the request is not POST.
    form = SignUpForm()
    context = {
        'title': title,
        'registration_form': form,
    }
    return render(request, template_name, context)


@login_required(login_url='account:login')
def user_logout(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('main:main-index')


@login_required(login_url='account:login')
def dashboard(request):
    title = 'User Dashboard'
    template_name = 'account/dashboard.html'
    user_contacts = Contact.objects.all().order_by(
        '-contact_date').filter(user_id=request.user.id)
    context = {
        'title': title,
        'user_contacts': user_contacts
    }
    return render(request, template_name, context)
