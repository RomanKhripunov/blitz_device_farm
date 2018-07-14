from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        required=True,
        label='Domain name'
    )
    email = forms.EmailField(required=True)
    room = forms.IntegerField(
        required=True,
        min_value=300,
        max_value=1699
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'room',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.room = self.cleaned_data['room']

        if commit:
            user.save()

        return user
