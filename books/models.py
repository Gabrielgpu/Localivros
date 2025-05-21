from django.conf import settings
from django.db import models

class Book(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='livros'
    )

    isbn = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=255, blank=True)
    gtin_ean = models.CharField(max_length=255, blank=True)
    width = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    depth = models.CharField(max_length=100, blank=True)
    mark = models.CharField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)
    url_external_images = models.TextField(blank=True)
    product_category = models.CharField(max_length=255, blank=True)
    additional_information = models.TextField(blank=True)
    ano_de_publicacao = models.CharField(max_length=4, blank=True)
    page_of_number = models.CharField(max_length=10, blank=True)
    author = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=100, blank=True)
    isbn10 = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.short_description or self.author or 'Livro'
