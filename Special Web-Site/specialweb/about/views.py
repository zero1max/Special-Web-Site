from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
#
from .models import User, Introduction, AboutMe, ComeJoinUs,\
      StudentsResults, StudentsTop5Results, Experience, Education, Courses


class HomeView(ListView):
    model = User
    template_name = 'about/index.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intros']  = Introduction.objects.all()
        context['abouts'] = AboutMe.objects.all()
        context['joins'] = ComeJoinUs.objects.all()
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.all()
        context['results'] = StudentsResults.objects.all()
        context['top5s'] = StudentsTop5Results.objects.all()
        context['courses'] = Courses.objects.all()
        return context