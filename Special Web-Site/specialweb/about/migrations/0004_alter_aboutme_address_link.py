# Generated by Django 5.0.6 on 2024-06-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_user_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='address_link',
            field=models.URLField(max_length=555, verbose_name='Manzil havolasi'),
        ),
    ]
