from django import forms
from . models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobileno': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            #'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        fields = [
            'name',
            'mobileno',
            'gender',
            'email',
            'password'
        ]