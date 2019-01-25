from allauth.account.forms import SignupForm
from django import forms


class ContactForm(forms.Form):
    name  = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    type = forms.ChoiceField()