from django import forms
from .models import UserProfile

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

class TeacherEditForm(forms.ModelForm):
 
    class Meta():
        model = UserProfile
        fields = "__all__"
        widgets = {
            'p_id': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'شماره شناسنامه'}),
            'f_name': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'نام پدر'}),
            'n_id': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'کد ملی'}),
            'birthday': forms.NumberInput(attrs={'class':'form-control text-left', 'placeholder':'سال تولد'}),
            'file_number': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'کد پیگیری'}),
            'degree': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'مدرک تحصیلی'}),
            'university': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'دانشگاه'}),
            'field': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'رشته'}),
            'rank': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'رتبه علمی'}),
            'job': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'شغل'}),
            'address': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'آدرس'}),
            't_year': forms.NumberInput(attrs={'class':'form-control text-left', 'placeholder':'سابقه تدریس'}),
            'phone': forms.NumberInput(attrs={'class':'form-control text-left', 'placeholder':'شماره تلفن'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control text-left', 'placeholder':'شماره همراه'}),
            'account': forms.NumberInput(attrs={'class':'form-control text-left', 'placeholder':'شماره حساب'}),
            'bank': forms.TextInput(attrs={'class':'form-control text-left', 'placeholder':'بانک'}),
        }