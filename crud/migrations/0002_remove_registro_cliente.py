# Generated by Django 3.2.9 on 2021-11-22 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='cliente',
        ),
    ]
