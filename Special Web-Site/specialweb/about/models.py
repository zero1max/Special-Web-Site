from django.db import models

class User(models.Model):
    name = models.CharField(max_length=155, verbose_name='Ism')
    admin = models.TextField()
    is_published = models.BooleanField(default=True, verbose_name='Nashr qilingan')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Rasm')

    def __str__(self):
        return self.name


class Introduction(models.Model):
    description = models.TextField(verbose_name='Tavsif')
    yellow_description = models.TextField(verbose_name='Sariq tavsif')
    yd_link = models.URLField(verbose_name='Sariq tavsif havolasi')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class AboutMe(models.Model):
    description = models.TextField(verbose_name='Tavsif')
    name = models.CharField(max_length=155, verbose_name='Ism')
    birthday = models.DateField(verbose_name='Tug‘ilgan kun')
    age = models.IntegerField(verbose_name='Yosh')
    address = models.TextField(verbose_name='Manzil')
    address_link = models.URLField(verbose_name='Manzil havolasi', max_length=555)
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    email = models.EmailField(verbose_name='Elektron pochta')
    email_link = models.URLField(verbose_name='Elektron pochta havolasi')
    telegram = models.CharField(max_length=50, verbose_name='Telegram')
    tg_link = models.URLField(verbose_name='Telegram havolasi')
    vd_link = models.URLField(verbose_name='Video havola')

    def __str__(self):
        return self.name


class ComeJoinUs(models.Model):
    title = models.CharField(max_length=155, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsif')
    address = models.TextField(verbose_name='Manzil')
    address_link = models.TextField(max_length=555 ,verbose_name='Manzil havolasi')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    email = models.TextField(verbose_name='Telegram')
    email_link = models.TextField(max_length=555 ,verbose_name='Telegram havolasi')

    def __str__(self):
        return self.title


class Experience(models.Model):
    wheredidyouwork = models.TextField(verbose_name='Where')
    role = models.TextField(verbose_name='Role')
    description = models.TextField(verbose_name='Description')
    is_published = models.BooleanField(default=True, verbose_name='Nashr qilish')
    start_date = models.TextField(verbose_name='Start')
    end_date = models.TextField(verbose_name='End')

    def __str__(self):
        return self.role


class Education(models.Model):
    wheredidyoulearn = models.TextField(verbose_name='Where')
    course = models.TextField(verbose_name='Kurs')
    description = models.TextField(verbose_name='Description')
    is_published = models.BooleanField(default=True, verbose_name='Nashr qilish')
    start_date = models.TextField(verbose_name='Start')
    end_date = models.TextField(verbose_name='End')

    def __str__(self):
        return self.course


class StudentsTop5Results(models.Model):
    name = models.CharField(max_length=155, verbose_name='Talaba ismi')
    overall = models.CharField(max_length=155, verbose_name='Umumiy natija')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Rasm')
    is_published = models.BooleanField(default=True, verbose_name='Nashr qilingan')

    def __str__(self):
        return self.name
  
    
class Courses(models.Model):
    course = models.TextField(verbose_name='Kurs')
    description = models.TextField(verbose_name='Tavsif')
    is_published = models.BooleanField(default=True, verbose_name='Nashr qilish')
    price = models.TextField('Price')

    def __str__(self):
        return self.course


class StudentsResults(models.Model):
    name = models.CharField(max_length=155, verbose_name='Ism')
    datatime = models.TextField(verbose_name='Sana va vaqt')
    description = models.TextField(verbose_name='Tavsif')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Rasm')
    is_published = models.BooleanField(default=True, verbose_name='Nashr qilingan')

    def __str__(self):
        return self.name
