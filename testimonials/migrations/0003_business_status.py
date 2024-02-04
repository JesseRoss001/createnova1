# Generated by Django 5.0.1 on 2024-02-04 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_servicepackage_business_delete_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('email_sent', 'Email Sent'), ('completed', 'Completed')], default='pending', max_length=12),
        ),
    ]