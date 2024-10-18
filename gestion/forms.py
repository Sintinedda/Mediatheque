from django import forms
from django.template.defaulttags import querystring

from gestion.models import Media, Borrower


# MEDIAS

class AddMediaForm(forms.Form):
    name = forms.CharField(required=True)


class UpdateMediaForm(forms.Form):
    name = forms.CharField(required=True)


# ITEMS

class AddItemForm(forms.Form):
    name = forms.CharField(required=True)
    author = forms.CharField(required=True)


class UpdateItemForm(forms.Form):
    name = forms.CharField(required=True)
    author = forms.CharField(required=True)
    category = forms.ModelChoiceField(queryset=Media.objects.all())


class LendItemForm(forms.Form):
    membre = forms.ModelChoiceField(queryset=Borrower.objects.filter(blocked=False))