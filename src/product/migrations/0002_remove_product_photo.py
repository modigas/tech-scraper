# Generated by Django 2.1.5 on 2021-01-05 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
    ]