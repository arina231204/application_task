from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect

from .mixins import FormControlMixin
from .models import Application


class ApplicationForm( forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Application
        fields = '__all__'




