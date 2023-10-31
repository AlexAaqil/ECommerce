from django.shortcuts import render, redirect
from userauths.forms import UserSignupForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings


User = settings.AUTH_USER_MODEL


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
        except:
            messages.warning(request, f"User with {email} does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("core:index")
        else:
            messages.warning(request, "User does not exist, create an account!")

    return render(request, 'userauths/login.html')

