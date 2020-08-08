from django import forms
from .models import UserProfile, Lesson

DEGREE_CHOICES = (
        ('کارشناسی', 'کارشناسی'),
        ('کارشناسی ارشد', 'کارشناسی ارشد'),
        ('دکتری', 'دکتری')
    )
RANK_CHOICES = (
        ('مربی', 'مربی'),
        ('استادیار', 'استادیار'),
        ('دانشیار', 'دانشیار'),
        ('استاد', 'استاد'),
    )
SEX_CHOICES = (
    ('آقا', 'آقا'),
    ('خانم', 'خانم')
)
GRADE_CHOICES = (
    ('کاردانی', 'کاردانی'),
    ('کارشناسی', 'کارشناسی')
)
    
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
    p_id = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شماره شناسنامه'
    }))
    f_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'نام پدر'
    }))
    n_id = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'کد ملی'
    }))
    birthday = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'سال تولد'
    }))
    file_number = forms.CharField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'کد پیگیری'
    }))
    degree = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'مدرک تحصیلی'
    }), choices=DEGREE_CHOICES)
    university = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'دانشگاه'
    }))
    field = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'رشته'
    }))
    rank = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'رتبه علمی'
    }), choices=RANK_CHOICES)
    job = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شغل'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'آدرس'
    }))
    t_year = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'سابقه تدریس'
    }))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شماره تلفن'
    }))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شماره همراه'
    }))
    account = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'شماره حساب'
    }))
    bank = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'بانک'
    }))
    sex = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'جنسیت'
    }), choices=SEX_CHOICES)

    class Meta():
        model = UserProfile
        fields = [
            'p_id', 'f_name', 'n_id', 'birthday', 'file_number', 'degree', 'university', 'field', 'rank',
            'job', 'address', 't_year', 'phone', 'mobile', 'account', 'bank', 'sex'
        ]


class LessonForm(forms.ModelForm):
    # user = forms.CharField(required=False)
    course_title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'عنوان دوره'
    }))
    grade = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control text-left',
        'placeholder':'عنوان دوره'
    }), choices=GRADE_CHOICES)
    lesson_title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-left',
        'placeholder':'عنوان درس'
    }))
    theorical_unit = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'تعداد واحد نظری'
    }))
    practical_unit = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'تعداد واحد عملی'
    }))
    theorical_time = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'ساعت نظری'
    }))
    practical_time = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'ساعت عملی'
    }))
    group = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control text-left',
        'placeholder':'گروه'
    }))
    class Meta():
        model = Lesson
        fields = [
            'course_title', 'grade', 'lesson_title', 'theorical_unit', 'theorical_time',
            'practical_unit', 'practical_time', 'group'
        ]