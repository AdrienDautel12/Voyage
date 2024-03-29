# Generated by Django 5.0.2 on 2024-02-29 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_user_personne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hebergement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_hebergement', models.CharField(max_length=100)),
                ('date_arrivee', models.DateField()),
                ('date_depart', models.DateField()),
                ('prix_nuit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moyen_transport', models.CharField(max_length=10)),
                ('date_depart', models.DateTimeField()),
                ('date_arrivee', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='personne',
            name='password',
        ),
        migrations.AddField(
            model_name='personne',
            name='adresse_rue',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='personne',
            name='adresse_ville',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='personne',
            name='date_naissance',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='personne',
            name='lieu_naissance',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='personne',
            name='nom',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='personne',
            name='prenom',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='personne',
            name='tel',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='personne',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=100)),
                ('date_reservation', models.DateTimeField(auto_now_add=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nb_passagers', models.PositiveIntegerField(default=1)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.personne')),
            ],
        ),
    ]
