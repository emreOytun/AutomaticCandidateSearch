from socket import fromshare
from django import forms
from django.forms import formset_factory

class LanguageForm(forms.Form) :
    language = forms.CharField(
        label = 'Language',
        widget=forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Enter a language here'
        })
    )

LanguageFormset = formset_factory(LanguageForm, extra = 1)