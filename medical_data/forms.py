from django import forms
from .models import MedicalProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = MedicalProfile
        exclude = ('user',)