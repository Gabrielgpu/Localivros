# Generated by Django 5.2.1 on 2025-05-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_ano_de_publicacao_book_year_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_published',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
