# Generated by Django 5.0.2 on 2024-02-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_activite_date_alter_hebergement_date_arrivee_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Activite',
        ),
        migrations.DeleteModel(
            name='Hebergement',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='utilisateur',
        ),
        migrations.DeleteModel(
            name='Voyage',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
