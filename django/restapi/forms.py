from django import forms


class GardenForm(forms.Form):
    image = forms.ImageField()
