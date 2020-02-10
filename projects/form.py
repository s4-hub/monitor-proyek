from django import forms
from .models import DaftarProject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = DaftarProject
        fields = [
            'nama','spk','sumber','alamat',
            'kota','provinsi','nilai',
            'tgl_mulai','tgl_selesai'
        ]

        widgets = {
            'nama': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Input Nama Proyek'}),
            'spk': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Input No SPK'}),
            'sumber': forms.Select(
                attrs={'class': 'form-control'
                }),
            'alamat': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Alamat'}),
            'kota': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Kota'}),
            'provinsi': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Provinsi'}),
            'nilai': forms.TextInput(
                attrs={'class': 'form-control',
                'placeholder': 'Nilai Proyek',
                'type': 'number'}),
            'tgl_mulai': forms.TextInput(
                attrs={'class': 'form-control',
                'type': 'date'}),
            'tgl_selesai': forms.TextInput(
                attrs={'class': 'form-control',
                'type': 'date'})
        }