# Generated by Django 5.2 on 2025-04-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0016_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
