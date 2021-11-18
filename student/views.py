from django.shortcuts import render

from .forms import StudentForm
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    # form_class = StudentForm  / this is instead of the last two rows
    # success_url = '/thanks/' / Eather success url or get_absolute_url must be provided to return the success page.
    template_name = "student/student_form.html" # this template name is created by default, but named by developer for reminding


    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass', 'id':'myid'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form

class ThanksTemplateView(TemplateView):
    template_name = 'student/thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksTemplateView,self).get_context_data(**kwargs)
        context['all_users'] = Student.objects.all()
        return context

class StudentDetailView(DetailView):
    model = Student

