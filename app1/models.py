from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    date_naissance = models.DateField( null=True)
    lieu_naissance = models.CharField(max_length=100, null=True)
    adresse_rue = models.CharField(max_length=255, null=True)
    adresse_ville = models.CharField(max_length=100, null=True)

class Voyage(models.Model):
    
    moyen_transport = models.CharField(max_length=10, null=True)
    date_depart = models.DateTimeField(null=True)
    date_arrivee = models.DateTimeField(null=True)
    

class Reservation(models.Model):
    utilisateur = models.ForeignKey(Personne, on_delete=models.CASCADE, null=True)
    lieu = models.CharField(max_length=100,null=True)
    date_reservation = models.DateTimeField(auto_now_add=True,null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    nb_passagers = models.PositiveIntegerField(default=1,null=True)

class Hebergement(models.Model):
    
    type_hebergement = models.CharField(max_length=100,null=True)
    date_arrivee = models.DateField(null=True)
    date_depart = models.DateField(null=True)
    prix_nuit = models.DecimalField(max_digits=10, decimal_places=2,null=True)

class Activite(models.Model):
    lieu = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2,null=True)

