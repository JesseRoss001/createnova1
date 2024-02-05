# Generated by Django 5.0.1 on 2024-02-05 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_business_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='business',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]