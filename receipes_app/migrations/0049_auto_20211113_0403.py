# Generated by Django 3.2.9 on 2021-11-13 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0048_alter_ingredient_grocery_aisle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuisine',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='diet',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='receipe',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['information']},
        ),
    ]
