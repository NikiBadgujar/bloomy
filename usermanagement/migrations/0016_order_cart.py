# Generated by Django 5.2 on 2025-04-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0015_remove_order_flower'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.JSONField(null=True),
        ),
    ]
