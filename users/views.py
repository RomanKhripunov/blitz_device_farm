from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

from .forms import RegistrationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def register(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('devices_farm:devices'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required()
def view_profile(request):
    context = {'user': request.user}
    return render(request, 'users/profile.html', context)


# TODO: need define
@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/view_profile')
    else:
        form = UserChangeForm(instance=request.user)
    return None
