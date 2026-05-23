from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import User
from .forms import *


class AccountDetailsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account_details_page.html', {'user': request.user})


class SignupView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = SignupForm()
            return render(request, 'signup_page.html', {'form': form})
        messages.info(request, 'You are already signed in.')
        return redirect('home_page')

    def post(self, request):
        if not request.user.is_authenticated:
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = make_password(form.cleaned_data['password'])
                user = User.objects.create(
                    username=username,
                    email=email,
                    password=password,
                )
                login(request, user)
                messages.success(request, 'You have successfully signed up! Welcome to F1 MotorSports.')
                return redirect('home_page')
            messages.error(request, 'Signup failed. Please fix the errors below.')
            return render(request, 'signup_page.html', {'form': form})
        messages.info(request, 'You are already signed in.')
        return redirect('home_page')


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request, 'login_page.html', {'form': form})
        messages.info(request, 'You are already signed in.')
        return redirect('home_page')

    def post(self, request):
        if not request.user.is_authenticated:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, 'You have successfully logged in!')
                    return redirect('home_page')
                messages.error(request, 'Login failed. Please check your username and password.')
            else:
                messages.error(request, 'Login failed. Please fix the errors below.')
            return render(request, 'login_page.html', {'form': form})
        messages.info(request, 'You are already signed in.')
        return redirect('home_page')


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'logout_page.html', {})
        messages.error(request, 'You are not logged in.')
        return redirect('home_page')

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'You have successfully logged out.')
            return redirect('home_page')
        messages.error(request, 'You are not logged in.')
        return redirect('home_page')
