__author__ = 'h_hack'
from .models import filemodel
from django import forms

class fileform(forms.ModelForm):
    class Meta:
        model= filemodel
        fields = ('image_title','image')