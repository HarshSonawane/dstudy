from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from . models import Profile


class EditProfileForm(UserChangeForm):
    template_name='user/edit_profile.html'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )