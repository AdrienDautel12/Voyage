# Generated by Django 5.0.2 on 2024-02-29 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_delete_activite_delete_hebergement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='date_naissance',
        ),
    ]
