from django.urls import path
from . import views

urlpatterns = [
    path("auth/bling/", views.AuthBlingView.as_view(), name="auth_bling"),
    path("auth/bling/callback/", views.AuthBlingCallbackView.as_view(), name="auth_bling_callback"),
    path("auth/bling/sendbook", views.SendProductToBlingView.as_view(), name="bling_send_book"),
    path("auth/bling/credentials", views.CredentialsBlingToIntegrationCreateView.as_view(), name="bling_credentials"),
    path("auth/bling/credential/<int:id>", views.EditCredentialsBlingUpdateView.as_view(), name="update_credential"),
]