from django.db import models


class Client(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nomClient = models.CharField(max_length=50)
    telClient = models.CharField(max_length=50)


class Cdr(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    date = models.DateField()
    duree = models.IntegerField()
    idClient=models.ForeignKey(Client,on_delete=models.CASCADE)

class Facture(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    montant=models.FloatField()
    dureeTotal = models.IntegerField()
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)

