from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    nif = models.CharField(max_length=9)
    cc = models.CharField(max_length=8)
    email = models.EmailField()




