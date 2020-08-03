from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_id = models.IntegerField(default=0)
    f_name = models.CharField(max_length=16, blank=True)
    birthday = models.IntegerField(default=0)
    n_id = models.IntegerField(default=0)
    file_number = models.IntegerField(default=0)
    degree = models.CharField(max_length=64, blank=True)
    field = models.CharField(max_length=64, blank=True)
    university = models.CharField(max_length=64, blank=True)
    rank = models.CharField(max_length=32, blank=True)
    job = models.CharField(max_length=64, blank=True)
    t_year = models.IntegerField(default=0)
    address = models.CharField(max_length=256, blank=True) 
    mobile = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    account = models.IntegerField(default=0)
    bank = models.CharField(max_length=16, blank=True)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Lesson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=64)
    grade = models.CharField(max_length=32)
    lesson_title = models.CharField(max_length=64)
    theorical_unit = models.IntegerField(default=0)
    practical_unit = models.IntegerField(default=0)
    theorical_time = models.IntegerField(default=0)
    practical_time = models.IntegerField(default=0)
    group = models.IntegerField(default=1)
