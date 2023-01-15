from django import forms

class EditUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    
