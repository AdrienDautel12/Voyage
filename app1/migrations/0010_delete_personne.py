# Generated by Django 5.0.2 on 2024-02-29 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_personne_date_naissance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personne',
        ),
    ]
