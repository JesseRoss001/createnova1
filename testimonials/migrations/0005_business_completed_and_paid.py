# Generated by Django 5.0.1 on 2024-02-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_business_is_sold_business_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='completed_and_paid',
            field=models.BooleanField(default=False),
        ),
    ]
