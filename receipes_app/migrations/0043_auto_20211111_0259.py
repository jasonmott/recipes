# Generated by Django 3.2.9 on 2021-11-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0042_receipe_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='cuisine',
        ),
        migrations.AddField(
            model_name='receipe',
            name='cuisine',
            field=models.ManyToManyField(blank=True, to='receipes_app.Cuisine'),
        ),
    ]
