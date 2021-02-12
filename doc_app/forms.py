from django.contrib.auth.models import User
from django import forms


class AddUserForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    repeatPassword = forms.CharField(max_length=64, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeatPassword')
        login = cleaned_data.get('login')
        if password != repeat_password:
            raise forms.ValidationError("Wrong Password!")
        try:
            user = User.objects.get(username=login)
        except User.DoesNotExist:
            return None
        if user.username == login:
            raise forms.ValidationError("Given login already in Data Base")


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class AddDocumentForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.Textarea()
    path = forms.FileField()


class AddAttributeForm(forms.Form):
    key = forms.CharField(max_length=255)
    value = forms.TextInput()
