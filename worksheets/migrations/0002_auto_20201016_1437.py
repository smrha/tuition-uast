# Generated by Django 3.0.8 on 2020-10-16 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worksheets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('text', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='degree',
            field=models.CharField(choices=[('کاردانی', 'کاردانی'), ('کارشناسی ناپیوسته', 'کارشناسی ناپیوسته')], default='کاردانی', max_length=64),
        ),
        migrations.CreateModel(
            name='ProjectQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('-', '-'), ('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('غیر قابل قبول', 'غیر قابل قبول')], default='-', max_length=16)),
                ('description', models.CharField(blank=True, max_length=64)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worksheets.Project')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worksheets.QuestionType')),
            ],
        ),
    ]
