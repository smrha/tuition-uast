from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control text-left',
            'placeholder':'نام کاربری'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control text-left',
            'placeholder':'رمز ورود'
    }   ))