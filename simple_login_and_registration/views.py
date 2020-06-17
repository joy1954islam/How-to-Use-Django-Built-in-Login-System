from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from simple_login_and_registration.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required




def home(request):
    if request.user.is_authenticated:
         messages.success(request,"Login Successfully")
         return redirect('profile')
    return HttpResponse("login failed")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'simple_login_and_registraion/register.html', {'form': form})


def BaseHome(request):
    return render(request,'Base.html',)


def Profile(request):
    return render(request,'simple_login_and_registraion/profile.html',)


def ChangeProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'simple_login_and_registraion/change_profile.html', context)


