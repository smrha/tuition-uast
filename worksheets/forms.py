from django import forms
from .models import Project

DEGREE_CHOICES = (
        ('کاردانی', 'کاردانی'),
        ('کارشناسی ناپیوسته', 'کارشناسی ناپیوسته'),
    )
QUESTION_CHOICES = (
    ('-', '-'),
    ('عالی', 'عالی'),
    ('خوب', 'خوب'),
    ('متوسط', 'متوسط'),
    ('غیر قابل قبول', 'غیر قابل قبول'),
)

class ProjectForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'نام'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'نام خانوادگی'
    }))
    std_id = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شماره دانشجویی'
    }))
    n_id = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شماره ملی'
    }))
    degree = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'مدرک تحصیلی'
    }), choices=DEGREE_CHOICES)
    field = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'رشته'
    }))
    start_date = forms.DateField(input_formats=["%Y/%m/%d"] ,widget=forms.DateInput(attrs={
        'class':'form-control text-left',
        'placeholder':'تاریخ شروع پروژه',
        'id': 'date1'
    }))
    end_date = forms.DateField(input_formats=["%Y/%m/%d"] ,widget=forms.DateInput(attrs={
        'class':'form-control text-left',
        'placeholder':'تاریخ پایان پروژه',
        'id': 'date2'
    }))
    value_question1 = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'پاسخ 1'
    }), choices=QUESTION_CHOICES)
    desc_question1 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'توضیحات'
    }), required=False)
    value_question2 = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'پاسخ 2'
    }), choices=QUESTION_CHOICES)
    desc_question2 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'توضیحات'
    }), required=False)
    value_question3 = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'پاسخ 3'
    }), choices=QUESTION_CHOICES)
    desc_question3 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'توضیحات'
    }), required=False)
    value_question4 = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'پاسخ 4'
    }), choices=QUESTION_CHOICES)
    desc_question4 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'توضیحات'
    }), required=False)
    score = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'نمره'
    }))
    score_letters = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'نمره به حروف'
    }))

    class Meta():
        model = Project
        fields = [
            'first_name', 'last_name', 'std_id', 'n_id', 'field', 'degree',
            'start_date', 'end_date', 'score_letters', 'score',
            'value_question1', 'value_question2', 'value_question3', 'value_question4',
            'desc_question1', 'desc_question2', 'desc_question3', 'desc_question4'
        ]

    