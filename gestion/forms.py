from django import forms


                                          # CATEGORY

class AddCatForm(forms.Form):
    name = forms.CharField(label='Nom', required=True)


class EditCatForm(forms.Form):
    name = forms.CharField(label='Nom', required=True)