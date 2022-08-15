from django import forms


class ClienteForm(forms.Form):
    email = forms.EmailField(label='Email')
    user = forms.CharField(label='Usuario')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    customer_id = forms.IntegerField(label='Customer ID')
