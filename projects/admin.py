from django.contrib import admin
from .models import DaftarProject

# Register your models here.

@admin.register(DaftarProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'nama','spk','sumber','alamat','kota',
        'nilai','tgl_buat','tgl_mulai','tgl_selesai'
    ]

    list_filter = [
        'nama','spk','tgl_buat','tgl_mulai','tgl_selesai'
    ]
