# Generated by Django 5.2 on 2025-04-26 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0014_order_flower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='flower',
        ),
    ]
