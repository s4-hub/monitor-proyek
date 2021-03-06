from django.db import models
from datetime import timedelta
import datetime, time
from django.contrib.auth.models import User

# Create your models here.
SUMBER_PROJECT = [
    (1, 'APBN'),
    (2, 'APBD TK. 1'),
    (3, 'APBD TK. 2'),
    (4, 'SWASTA'),
    (5, 'DANA INTERNASIONAL')
]

class DaftarProject(models.Model):
    nama = models.CharField(max_length=200, blank=False, verbose_name='NAMA PROJECT')
    spk = models.CharField(max_length=30, verbose_name='NO SPK')
    sumber = models.IntegerField(choices=SUMBER_PROJECT)
    alamat = models.CharField(max_length=200, blank=False)
    kota = models.CharField(max_length=100, blank=False, verbose_name='KOTA/KABUPATEN')
    provinsi = models.CharField(max_length=30)
    nilai = models.FloatField(verbose_name='NILAI PROJECT')
    tgl_buat = models.DateField(auto_now=True)
    tgl_mulai = models.DateField()
    tgl_selesai = models.DateField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def jatuh_tempo(self):
    
        if (self.tgl_mulai == datetime.date.today()) or (self.tgl_mulai < datetime.date.today()):
           selisih = self.tgl_selesai - datetime.date.today()
        else:
           selisih = self.tgl_selesai - self.tgl_mulai
      
        
        return (selisih.days)

        