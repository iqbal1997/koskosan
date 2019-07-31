from django.db import models

# Create your models here.
class Admin(models.Model):
    NamaLengkap = models.CharField(max_length=30)
    NoTelp = models.CharField(max_length=10)
    NoHP = models.CharField(max_length=20)
    Provinsi = models.CharField(max_length=30)
    kota = models.CharField(max_length=30)
    Alamat = models.TextField()
    KodePos = models.CharField(max_length=10)
    Email = models.CharField(max_length=20)

    def __str__(self):
        return self.NamaLengkap