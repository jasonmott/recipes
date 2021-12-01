# Generated by Django 3.2.9 on 2021-11-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0028_remove_receipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='image_URL',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='receipe',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipe',
            name='source_URL',
            field=models.URLField(blank=True),
        ),
    ]