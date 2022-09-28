from contextlib import nullcontext
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from tokenize import *

class Produk(models.Model):
    jasa = models.CharField(max_length=240)
    harga = models.IntegerField()

    def __str__(self):
        return self.jasa
    class Meta:
        db_table = "produk"

class Konsumen(models.Model):
    nama = models.CharField(max_length=40)
    alamat = models.CharField(max_length=240)
    hp = models.IntegerField()
    produk = models.ForeignKey(Produk, default="Free", verbose_name="produk_id", on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nama 
    class Meta:
        db_table = "konsumen"
        