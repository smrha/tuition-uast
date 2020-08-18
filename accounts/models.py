from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_id = models.CharField(max_length=10, blank=True)
    f_name = models.CharField(max_length=16, blank=True)
    birthday = models.IntegerField(default=0)
    n_id = models.CharField(max_length=10, blank=True)
    file_number = models.CharField(max_length=16, blank=True)
    degree = models.CharField(max_length=64, choices=DEGREE_CHOICES, default='کارشناسی')
    field = models.CharField(max_length=64, blank=True)
    university = models.CharField(max_length=64, blank=True)
    rank = models.CharField(max_length=32, choices=RANK_CHOICES, default='مربی')
    job = models.CharField(max_length=64, blank=True)
    t_year = models.IntegerField(default=0)
    address = models.CharField(max_length=256, blank=True) 
    mobile = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    account = models.IntegerField(default=0)
    bank = models.CharField(max_length=16, blank=True)
    sex = models.CharField(max_length=8, choices=SEX_CHOICES, default='آقا')
    theorical_pay = models.IntegerField(default=0)
    practical_pay = models.IntegerField(default=0)
    sign = models.ImageField(null=True, blank=True)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=64)
    grade = models.CharField(max_length=32, choices=GRADE_CHOICES, default='کاردانی')
    lesson_title = models.CharField(max_length=64)
    theorical_unit = models.IntegerField(default=0)
    practical_unit = models.IntegerField(default=0)
    theorical_time = models.IntegerField(default=0)
    practical_time = models.IntegerField(default=0)
    group = models.IntegerField(default=1)

class Lessonaccepted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
