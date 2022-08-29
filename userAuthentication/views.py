from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect


def homepage(request):
    return render(request, 'userAuthentication/homepage.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'userAuthentication/base.html',
                          {'fname': fname})
        else:

            messages.error(request, 'Incorrect credentials Entered')
            return redirect('homepage')

    return render(request, 'userAuthentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'User logged out!')
    return redirect('homepage')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        lname = request.POST['lname']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken!\n')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                        password=pass1, email=email, first_name=fname,
                        last_name=lname)
                user.save()
                messages.success(request,
                                 'Account Created Successfully!')
                return redirect('signin')
        else:
            messages.error(request, 'password do not match! \n')
            return redirect('signup')
    else:
        return render(request, 'userAuthentication/signup.html')
