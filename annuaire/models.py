from django.db import models

class Contact (models.Model):
   nom = models.CharField(max_length=50, blank=False, null=False)
   prenom = models.CharField(max_length=50, blank=True, null=True)
   telephone = models.CharField(max_length=15, blank=False, null=False)
   entreprise = models.BooleanField( blank=False, null=False, default=False)