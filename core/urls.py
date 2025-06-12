from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scraping.urls')),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('api/v1/', include('integrator.urls'))
]
