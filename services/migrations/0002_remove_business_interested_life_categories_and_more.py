# Generated by Django 5.0.1 on 2024-02-03 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='interested_life_categories',
        ),
        migrations.DeleteModel(
            name='ServicePackage',
        ),
    ]
