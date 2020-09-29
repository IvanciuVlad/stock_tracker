from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy

from . import forms


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'