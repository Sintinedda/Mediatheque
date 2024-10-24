from django import forms

from gestion.models import Category


# CATEGORY

class AddCatForm(forms.Form):
    name = forms.CharField(label='Nom', required=True)


class EditCatForm(forms.Form):
    name = forms.CharField(label='Nom', required=True)


                                          # ITEM

class AddItemForm(forms.Form):
    name = forms.CharField(label='Nom', required=True)
    creator = forms.CharField(label='Auteur/Créateur', required=True)


class EditItemForm(forms.Form):
    name = forms.CharField(label='Nom', required=False)
    creator = forms.CharField(label='Auteur/Créateur', required = False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                    label='Catégorie')