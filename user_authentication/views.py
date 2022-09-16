from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import UpdateUserForm, Registeruser


def homepage(request):
    return render(request, "user_authentication/homepage.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "user_authentication/userbase.html", {"fname": fname})

        else:
            messages.error(request, "Incorrect credentials Entered")
            return redirect("homepage")

    return render(request, "user_authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "User logged out!")
    return redirect("homepage")


def signup(request):
    if request.method == "POST":
        form = Registeruser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
    else:
        form = Registeruser()

    return render(request, 'user_authentication/signup.html', {'form': form})


@login_required
def updateprofile(request):
    user = request.user
    print(user.username)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return redirect("updateprofile")
    else:
        form = UpdateUserForm()

    return render(request, 'user_authentication/updateprofile.html', {'form': form})
