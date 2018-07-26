from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import DetailView
from django.utils.decorators import method_decorator

from .models import User
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


class ProfileDetail(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/profile.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileDetail, self).dispatch(request, *args, **kwargs)


# TODO: need define
@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = UserChangeForm(instance=request.user)
    return None
