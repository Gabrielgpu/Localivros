from django import forms
from .models import Book

class EditBookForm(forms.ModelForm):
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Título Livro', 'class': 'form-control'}),
        label=''
    )

    short_description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Descrição Livro', 'class': 'form-control'}),
        label=''
    )

    year_published = forms.DateField(
        required=False,
        localize=True,
        widget=forms.DateInput(attrs={'placeholder': 'Ano Livro', 'class': 'form-control'}),
        input_formats=['%d/%m/%Y'],
        label=''
    )

    product_category = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Categoria Livro', 'class': 'form-control'}),
        label=''
    )

    price = forms.DecimalField(
        required=True,
        max_digits=6,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'Valor Livro', 'class': 'form-control'}),
        label=''
    )

    stock = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Estoque Livro', 'class': 'form-control'}),
        label=''
    )


    class Meta:
        model = Book
        fields = ('description', 'short_description', 'year_published', 'product_category', 'price', 'stock')



    