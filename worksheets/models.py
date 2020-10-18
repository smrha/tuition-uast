from django.db import models
from django.contrib.auth.models import User

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

class Project(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    std_id = models.IntegerField(default=0)
    n_id = models.IntegerField(default=0)
    field = models.CharField(max_length=64)
    degree = models.CharField(max_length=64, choices=DEGREE_CHOICES, default='کاردانی')
    start_date = models.DateField()
    end_date = models.DateField()
    score = models.IntegerField(default=0)
    score_letters = models.CharField(max_length=32)
    value_question1 = models.CharField(max_length=16, choices=QUESTION_CHOICES, default='-')
    value_question2 = models.CharField(max_length=16, choices=QUESTION_CHOICES, default='-')
    value_question3 = models.CharField(max_length=16, choices=QUESTION_CHOICES, default='-')
    value_question4 = models.CharField(max_length=16, choices=QUESTION_CHOICES, default='-')
    desc_question1 = models.CharField(max_length=64, blank=True)
    desc_question2 = models.CharField(max_length=64, blank=True)
    desc_question3 = models.CharField(max_length=64, blank=True)
    desc_question4 = models.CharField(max_length=64, blank=True)
# class QuestionType(models.Model):
#     name = models.CharField(max_length=32)
#     text = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name

# class ProjectQuestion(models.Model):
#     proj = models.ForeignKey(Project, on_delete=models.CASCADE)
#     question = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
#     value = models.CharField(max_length=16, choices=QUESTION_CHOICES, default='-')
#     description = models.CharField(max_length=64, blank=True)