# Generated by Django 5.1.6 on 2025-03-02 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_sell_book', 'Can add book'), ('can_buy_book', 'Can delete book'), ('can_publish_book', 'Can create book')]},
        ),
    ]
