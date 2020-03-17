from django.db import models
from projects.models import DaftarProject

# Create your models here.

class Pemasukan(models.Model):
    nama_proj = models.ForeignKey(DaftarProject, on_delete=models.CASCADE)
    tgl_proj = models.DateField()
    nominal = models.IntegerField()
    
                     
    