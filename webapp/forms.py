from django import forms


class Lastname(forms.Form):
    lastname = forms.CharField(label="Last name", max_length=20)
