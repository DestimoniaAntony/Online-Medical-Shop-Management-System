# Generated by Django 4.2.5 on 2023-10-12 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_assign_price_assign_req_qnty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pharmacy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_app.pharmacy'),
        ),
    ]
