from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import SignUpForm


class UserLoginView(LoginView):
  template_name = 'login.html'
  redirect_authenticated_user = True
  success_message = 'Login realizado com sucesso!'
  error_message = 'Usuário ou senha incorretos.'

  def get_success_url(self):
    return self.success_url
  
  def form_valid(self, form):
    messages.success(self.request, self.success_message)
    return super().form_valid(form)
  
  def form_invalid(self, form):
    messages.error(self.request, self.error_message)
    return super().form_invalid(form)


class UserLogoutView(LoginRequiredMixin, LogoutView):
  template_name = 'logout.html'
  success_message = 'Logout realizado com sucesso!'

  def dispatch(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super().dispatch(request, *args, **kwargs)

  def dispatch(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super().dispatch(request, *args, **kwargs)


class UserCreateView(SuccessMessageMixin, CreateView):
  form_class = SignUpForm
  template_name = 'register.html'
  success_url = reverse_lazy('products')
  success_message = 'Cadastro realizado com sucesso!'
