from django.contrib import admin
from .models import User, Introduction, AboutMe, ComeJoinUs,\
    StudentsResults, StudentsTop5Results, Education, Experience, Courses
from django.utils.html import format_html

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin', 'is_published', 'photo_tag']
    list_editable = ['is_published',]
    search_fields = ['name', 'admin']

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'
    
class IntroAdmin(admin.ModelAdmin):
    list_display = ['description', 'is_published', 'yd_link']
    list_editable = ['is_published',]


class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'age']


class ResultsTop5Admin(admin.ModelAdmin):
    list_display = ['name', 'overall', 'is_published', 'photo_tag']
    list_editable = ['is_published']

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'


class ResultsAdmin(admin.ModelAdmin):
    list_display = ['name', 'datatime', 'is_published', 'photo_tag']
    list_editable = ['is_published']

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'


class ComeJoinUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'phone', 'email']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['wheredidyouwork', 'role', 'is_published']
    list_editable = ['is_published']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['wheredidyoulearn', 'course', 'is_published']
    list_editable = ['is_published']

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['course', 'is_published']
    list_editable = ['is_published']


admin.site.register(User, UserAdmin)
admin.site.register(Introduction, IntroAdmin)
admin.site.register(AboutMe, AboutAdmin)
admin.site.register(ComeJoinUs, ComeJoinUsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(StudentsResults, ResultsAdmin)
admin.site.register(StudentsTop5Results, ResultsTop5Admin)
admin.site.register(Courses, CoursesAdmin)