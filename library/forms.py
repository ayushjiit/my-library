from django import forms

from .models import lib

class libform(forms.ModelForm):

    class Meta:
        model = lib
        fields = ('section', 'title', 'writer',)
