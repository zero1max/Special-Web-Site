# Generated by Django 5.0.6 on 2024-06-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentstop5results',
            name='title',
        ),
        migrations.AddField(
            model_name='introduction',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='address',
            field=models.TextField(verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='address_link',
            field=models.URLField(verbose_name='Manzil havolasi'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='age',
            field=models.IntegerField(verbose_name='Yosh'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='birthday',
            field=models.DateField(verbose_name='Tug‘ilgan kun'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Elektron pochta'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='email_link',
            field=models.URLField(verbose_name='Elektron pochta havolasi'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='telegram',
            field=models.CharField(max_length=50, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='tg_link',
            field=models.URLField(verbose_name='Telegram havolasi'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='vd_link',
            field=models.URLField(verbose_name='Video havola'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='address',
            field=models.TextField(verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='address_link',
            field=models.URLField(verbose_name='Manzil havolasi'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Elektron pochta'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='email_link',
            field=models.URLField(verbose_name='Elektron pochta havolasi'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='comejoinus',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='yd_link',
            field=models.URLField(verbose_name='Sariq tavsif havolasi'),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='yellow_description',
            field=models.TextField(verbose_name='Sariq tavsif'),
        ),
        migrations.AlterField(
            model_name='studentsresults',
            name='datatime',
            field=models.DateTimeField(verbose_name='Sana va vaqt'),
        ),
        migrations.AlterField(
            model_name='studentsresults',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='studentsresults',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Nashr qilingan'),
        ),
        migrations.AlterField(
            model_name='studentsresults',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='studentsresults',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='studentstop5results',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Nashr qilingan'),
        ),
        migrations.AlterField(
            model_name='studentstop5results',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Talaba ismi'),
        ),
        migrations.AlterField(
            model_name='studentstop5results',
            name='overall',
            field=models.CharField(max_length=155, verbose_name='Umumiy natija'),
        ),
        migrations.AlterField(
            model_name='studentstop5results',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Nashr qilingan'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Rasm'),
        ),
    ]
