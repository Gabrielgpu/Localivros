from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.conf import settings
from .models import ApiIntegrationToken, BlingCredential
from .services import bling
from books.models import Book
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from requests_oauthlib import OAuth2Session
from pathlib import Path
import pprint
import os


DIR = Path(__file__).resolve().parent


redirect_uri = settings.EXTERNAL_API_URI
token_url = settings.EXTERNAL_API_TOKEN_ENDPOINT
authorization_base_url = settings.EXTERNAL_API_AUTHORIZATION_END_POINT


class AuthBlingView(LoginRequiredMixin, View):

    def get(self, request):
        client_id, _ = BlingCredential.get_credentials()
        
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

        print(redirect_uri)

        oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=["*"])
        authorization_url, state = oauth.authorization_url(authorization_base_url)

        request.session["oauth_state"] = state
        return redirect(authorization_url)


class AuthBlingCallbackView(LoginRequiredMixin, View):
    success_message = 'Token armazenado no banco de dados'

    def get(self, request):
        client_id, client_secret = BlingCredential.get_credentials()

        oauth = OAuth2Session(
            client_id, 
            state=request.session.get("oauth_state"), 
            redirect_uri=redirect_uri
        )

        full_url = request.build_absolute_uri()

        token = oauth.fetch_token(
            token_url,
            authorization_response=full_url,
            client_secret=client_secret
        )


        ApiIntegrationToken.objects.create(
            access_token=token.get('access_token'),
            expires_in=token.get('expires_in'),
            refresh_token=token.get('refresh_token'),

        )
        
        messages.success(
            request, 
            self.success_message
        )

        return redirect('books')



class SendProductToBlingView(LoginRequiredMixin, View):

    def post(self, request):
        id = request.POST.get('id')

        book = Book.objects.filter(id=id).first()

        credentials_token = ApiIntegrationToken.objects.last()

        if credentials_token is None:
            return redirect('auth_bling')

        if not credentials_token.is_token_valid():
            token_valid = credentials_token.refresh()
            
            if not token_valid:
                messages.error(request, 'Problemas para fazer refresh token')
                return redirect('book_search')

        product_response = bling.create_product(book, credentials_token.access_token)
        if product_response.status_code != 201:
            messages.error(request, 'Não foi possível cadastrar livro na Bling')
            return redirect('books')
        
        book.id_bling = product_response.json()["data"]["id"]
        book.save()
        messages.success(request, 'Livro cadastrado na Bling')


        bling = BlingCredential.objects.last()

        stock_response = bling.increment_stock(book, bling.deposit_id, credentials_token.access_token)
        if stock_response.status_code != 201:
            messages.error(request, 'houve erro ao atualizar estoque.')
            return redirect('books')

        messages.success(request, 'Estoque atualizado com sucesso!')
        return redirect('books')



class CredentialsBlingToIntegrationCreateView(SuccessMessageMixin, CreateView):
    model = BlingCredential
    template_name = 'integration_bling.html'
    success_url = reverse_lazy('books')
    success_message = "Credencial salva!"
    fields = ["client_id", "client_secret", "deposit_id"]


    def get(self, request, *args, **kwargs):
        if self.is_credential_registered():
            return render(request, 'update_credential.html', { 'credential': self.model.objects.last() })
        
        return super().get(request, *args, **kwargs)
    
    def is_credential_registered(self):
        credential = self.model.objects.last()
        if credential:
            return True
        
        return False

class EditCredentialsBlingUpdateView(SuccessMessageMixin, UpdateView):
    model = BlingCredential
    success_url = reverse_lazy("books")
    success_message = "Credenciais atualizadas com sucesso!"
    pk_url_kwarg = "id"
    fields = ["client_id", "client_secret", "deposit_id"]
