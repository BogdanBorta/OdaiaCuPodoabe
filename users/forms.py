from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')

        # Am adaugat clasa campurilor, pentru a le putea selecta in css(nu functioneaza)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'user_form'}),
            'last_name': forms.TextInput(attrs={'class': 'user_form'}),
            'username': forms.TextInput(attrs={'class': 'user_form'}),
            'email': forms.TextInput(attrs={'class': 'user_form'}),
            'password1': forms.TextInput(attrs={'class': 'user_form'}),
            'password2': forms.TextInput(attrs={'class': 'user_form'})
        }
