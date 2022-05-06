# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class ChangePassword(UpdateView):
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('login')
#     template_name = 'changepasswd.html'