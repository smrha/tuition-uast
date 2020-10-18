from django import forms
from .models import Term

class TermAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'عنوان ترم'
    }))
    start_date = forms.DateField(input_formats=["%Y/%m/%d"] ,widget=forms.DateInput(attrs={
        'class':'form-control text-left',
        'placeholder':'تاریخ شروع ترم',
        'id': 'date1'
    }))
    end_date = forms.DateField(input_formats=["%Y/%m/%d"] ,widget=forms.DateInput(attrs={
        'class':'form-control text-left',
        'placeholder':'تاریخ پایان ترم',
        'id': 'date2'
    }))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':'checkbox-input',
        'placeholder':'وضعیت ترم'
    }), required=False)

    class Meta():
        model = Term
        fields = ['name', 'start_date', 'end_date', 'is_active']