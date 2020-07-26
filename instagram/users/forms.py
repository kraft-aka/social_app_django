from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()



class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class OwnUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')
