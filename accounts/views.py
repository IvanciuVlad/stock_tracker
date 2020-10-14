from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy

from . import forms
from . import models

from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class UserList(ListView):
    model = models.User

    def get_queryset(self):
        return User.objects.all()
