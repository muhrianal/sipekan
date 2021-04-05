from django.db import models
from django.contrib.auth.models import User
from .izin_kegiatan import IzinKegiatan

class PermintaanProtokoler(models.Model):
    izin_kegiatan = models.OneToOneField(
        IzinKegiatan,
        on_delete=models.CASCADE
    )

    deskripsi_kebutuhan = models.CharField(max_length=500)

class PerizinanPublikasi(models.Model):
    izin_kegiatan = models.OneToOneField(
        IzinKegiatan,
        on_delete=models.CASCADE
    )
    tanggal_mulai = models.DateField()
    tanggal_akhir = models.DateField()
    
    STATUS_CHOICES = (
      (1, 'Menunggu Persetujuan'),
      (2, 'Disetujui'),
      (3, 'Ditolak'),
    )

    status_perizinan_publikasi = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    alasan_penolakan = models.CharField(max_length=500, default=None, blank=True, null=True)
    keterangan = models.CharField(max_length=500, default=None, blank=True, null=True)
    file_materi_kegiatan = models.FileField(upload_to='file_materi_kegiatan')
    file_flyer_pengumuman = models.FileField(upload_to='file_flyer_pengumuman')

class JenisPublikasi(models.Model):
    perizinan_publikasi = models.ForeignKey(
        PerizinanPublikasi,
        on_delete=models.CASCADE
    )

    deskripsi_publikasi = models.CharField(max_length=500)

class Souvenir(models.Model):
    nama_souvenir = models.CharField(max_length=255)
    
    KELAS_CHOICES = (
        (1, 'Kelas 1'),
        (2, 'Kelas 2'),
        (3, 'Kelas 3'),
        (4, 'Kelas 1 & Kelas 2'),
        (5, 'Kelas 1 & Kelas 3'),
        (6, 'Kelas 2 & Kelas 3'),
        (7, 'Kelas 1 & Kelas 2 & Kelas 3'),
    )

    kelas = models.PositiveSmallIntegerField(choices=KELAS_CHOICES)
    
    REGION_CHOICES = (
        (1, 'Dalam Negeri'),
        (2, 'Luar Negeri'),
        (3, 'Dalam dan Luar Negeri'),
    )
    region = models.PositiveSmallIntegerField(choices=KELAS_CHOICES)
    
    stok = models.IntegerField()

class PermintaanSouvenir(models.Model):
    izin_kegiatan = models.ForeignKey(
        IzinKegiatan,
        on_delete=models.CASCADE
    )
    alasan_penolakan = models.CharField(max_length=500, default=None, blank=True, null=True)
    
    STATUS_CHOICES = (
      (1, 'Menunggu Persetujuan'),
      (2, 'Disetujui'),
      (3, 'Ditolak'),
    )

    status_permintaan_souvenir = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    jumlah = models.IntegerField()
    souvenir = models.ForeignKey(
        Souvenir,
        on_delete=models.CASCADE
    )
    nama_penerima_souvenir = models.CharField(max_length=255)
    jabatan_penerima_souvenir = models.CharField(max_length=255)
    