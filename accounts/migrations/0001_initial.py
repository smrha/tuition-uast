# Generated by Django 3.0.8 on 2020-08-14 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=64)),
                ('grade', models.CharField(choices=[('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی')], default='کاردانی', max_length=32)),
                ('lesson_title', models.CharField(max_length=64)),
                ('theorical_unit', models.IntegerField(default=0)),
                ('practical_unit', models.IntegerField(default=0)),
                ('theorical_time', models.IntegerField(default=0)),
                ('practical_time', models.IntegerField(default=0)),
                ('group', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(blank=True, max_length=10)),
                ('f_name', models.CharField(blank=True, max_length=16)),
                ('birthday', models.IntegerField(default=0)),
                ('n_id', models.CharField(blank=True, max_length=10)),
                ('file_number', models.CharField(blank=True, max_length=16)),
                ('degree', models.CharField(choices=[('کارشناسی', 'کارشناسی'), ('کارشناسی ارشد', 'کارشناسی ارشد'), ('دکتری', 'دکتری')], default='کارشناسی', max_length=64)),
                ('field', models.CharField(blank=True, max_length=64)),
                ('university', models.CharField(blank=True, max_length=64)),
                ('rank', models.CharField(choices=[('مربی', 'مربی'), ('استادیار', 'استادیار'), ('دانشیار', 'دانشیار'), ('استاد', 'استاد')], default='مربی', max_length=32)),
                ('job', models.CharField(blank=True, max_length=64)),
                ('t_year', models.IntegerField(default=0)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('mobile', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('account', models.IntegerField(default=0)),
                ('bank', models.CharField(blank=True, max_length=16)),
                ('sex', models.CharField(choices=[('آقا', 'آقا'), ('خانم', 'خانم')], default='آقا', max_length=8)),
                ('theorical_pay', models.IntegerField(default=0)),
                ('practical_pay', models.IntegerField(default=0)),
                ('sign', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lessonaccepted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
