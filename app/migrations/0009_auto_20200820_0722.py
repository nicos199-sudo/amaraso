# Generated by Django 2.2.14 on 2020-08-20 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='payment_option',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='stripe_charge_id',
        ),
    ]
