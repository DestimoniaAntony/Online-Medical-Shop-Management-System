# Generated by Django 4.2.5 on 2023-10-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_assign_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assign',
            name='cart',
        ),
    ]
