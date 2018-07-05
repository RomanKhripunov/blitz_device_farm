from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm


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


# TODO: need to define
def profile(request):
    return None
