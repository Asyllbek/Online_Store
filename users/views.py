from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserCreationModelForm

User = get_user_model()


class UserRegistrationView(CreateView):
    form_class = UserCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'main_page/user_cabinet.html'

    def get_object(self):
        return User.objects.get(username=self.request.user.username)