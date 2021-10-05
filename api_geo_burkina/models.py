from django.db import models

# Create your models here.

class Departements(models.Model):
    nom = models.CharField(max_length=30)
    province = models.ForeignKey('Provinces',on_delete=models.CASCADE, related_name="departement", null=True)
    def __str__(self):
        return self.nom

class ChefLieuProvince(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Provinces(models.Model):
    nom = models.CharField(max_length=30)
    chef_lieu = models.OneToOneField('Departements', on_delete=models.CASCADE, related_name="chef_lieu")
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='province', null=True)

    def __str__(self):
        return self.nom

class Region(models.Model):
    nom = models.CharField(max_length=255)
    chef_lieu = models.OneToOneField(Departements, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

