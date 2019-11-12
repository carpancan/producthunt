from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import auth
from .user import registration
from .user.exceptions import CustomExceptions


@require_GET
def signup(request):
    return render(request, 'accounts/signup.html')


@require_POST
def register(request):
    try:
        new_user_dto = registration.NewUserDto(request.POST)
        new_user = registration.Register().create_user(new_user_dto)
        auth.login(request, new_user)
        return redirect('home')
    except CustomExceptions.UserExistsException as exception:
        result = exception.get_message()
        return render(request, 'accounts/signup.html', {'result': result})


@require_GET
def show_login(request):
    return render(request, 'accounts/login.html')


@require_POST
def login(request):
    try:
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        return render(request, 'accounts/login.html', {'result': 'Invalid credentials'})
    except Exception as exception:
        return render(request, 'accounts/login.html', {'result': exception})


@require_POST
def logout(request):
    auth.logout(request)
    return redirect('home')
