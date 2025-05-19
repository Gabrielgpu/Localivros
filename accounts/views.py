from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import SignUpForm


class UserLoginView(LoginView):
  template_name = 'login.html'
  redirect_authenticated_user = True
  success_message = 'Login realizado com sucesso!'
  error_message = 'Usuário ou senha incorretos.'

class UserLogoutView(LogoutView):
  template_name = 'logout.html'
  success_message = 'Logout realizado com sucesso!'

  def dispatch(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super().dispatch(request, *args, **kwargs)

class UserCreateView(CreateView):
  form_class = SignUpForm
  template_name = 'register.html'
  success_url = reverse_lazy('products')
  success_message = 'Cadastro realizado com sucesso!'
