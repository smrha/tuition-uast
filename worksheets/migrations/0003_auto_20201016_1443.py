# Generated by Django 3.0.8 on 2020-10-16 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worksheets', '0002_auto_20201016_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectquestion',
            old_name='project',
            new_name='proj',
        ),
    ]