# Generated by Django 5.0.6 on 2024-07-31 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_education_experience_alter_comejoinus_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='title',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='title',
        ),
    ]
