# Generated by Django 3.2.9 on 2021-11-11 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0036_auto_20211111_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuisine',
            name='grocery_aisle',
        ),
    ]
