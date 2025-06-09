from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.conf import settings
from .models import Credentials
from .services import bling
from books.models import Book

from requests_oauthlib import OAuth2Session
from pathlib import Path
import pprint
import os


DIR = Path(__file__).resolve().parent


client_id = settings.EXTERNAL_CLIENT_ID
redirect_uri = settings.EXTERNAL_API_URI
client_secret = settings.EXTERNAL_CLIENT_SECRET
token_url = settings.EXTERNAL_API_TOKEN_ENDPOINT
authorization_base_url = settings.EXTERNAL_API_AUTHORIZATION_END_POINT


class AuthBlingView(View):

    def get(self, request):
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

        oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=["*"])
        authorization_url, state = oauth.authorization_url(authorization_base_url)

        request.session["oauth_state"] = state

        return redirect(authorization_url)


class AuthBlingCallbackView(View):
    success_message = 'Token armazenado no banco de dados'

    def get(self, request):
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


        Credentials.objects.create(
            access_token=token.get('access_token'),
            expires_in=token.get('expires_in'),
            refresh_token=token.get('refresh_token'),

        )
        
        messages.success(
            request, 
            self.success_message
        )

        return redirect('books')



class SendProductToBlingView(View):

    def post(self, request):
        id = request.POST.get('id')

        model = Book.objects.filter(id=id).first()

        credentials = Credentials.objects.last()

        if not credentials.is_token_valid():
            token_valid = credentials.refresh()

            if not token_valid:
                messages.error(request, 'Problemas para fazer refresh token')
                return redirect('book_search')

        product_response = bling.create_product(model, credentials.access_token)
        if product_response.status_code != 201:
            messages.error(request, 'Não foi possível cadastrar livro na Bling')
            return redirect('books')
        
        model.id_bling = product_response.json()["data"]["id"]
        model.save()
        messages.success(request, 'Livro cadastrado na Bling')


        stock_response = bling.increment_stock(model, credentials.access_token)
        if stock_response.status_code != 201:
            messages.error(request, 'houve erro ao atualizar estoque.')
            return redirect('books')

        messages.success(request, 'Estoque atualizado com sucesso!')
        return redirect('books')