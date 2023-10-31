from django.shortcuts import render, redirect
from userauths.forms import UserSignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import User


def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, Your account was created Successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserSignupForm()

    context = {
        'form': form,
    }

    return render(request, 'userauths/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You're already logged in!!!")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("core:index")
            else:
                messages.warning(request, "User does not exist, create an account!")
        except:
            messages.warning(request, f"User with {email} does not exist")

    return render(request, 'userauths/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You've logged out. Login again to continue shopping.")
    return redirect("userauths:login")
