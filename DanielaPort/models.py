from django.db import models

class user(models.Model):
    nom=models.CharField( max_length=50)
    prenom=models.CharField(max_length=100)
    Age=models.CharField(max_length=35)
    numero=models.CharField(max_length=100)
    
    
class Contact(models.Model):
    identite = models.CharField(max_length=100)
    email = models.EmailField()
    type_projet = models.CharField(max_length=100)
    message = models.TextField()
    accepte_donnees = models.BooleanField()