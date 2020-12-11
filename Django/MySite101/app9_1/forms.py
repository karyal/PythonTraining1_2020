from django import forms


class PersonForm(forms.Form):
    full_name = forms.CharField()
    contact_address = forms.CharField()
    email = forms.CharField()
    mobile = forms.CharField()