from rest_framework import serializers 

from ..models.peminjaman_ruangan import PeminjamanRuangan
from ..models.izin_kegiatan import IzinKegiatan


class PeminjamanRuanganUnitKerjaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PeminjamanRuangan
        fields = (
            'id', 
            'created_at', 
            'updated_at', 
            'alasan_penolakan',
            'judul_peminjaman', 
            'status_peminjaman_ruangan', 
            'waktu_mulai', 
            'waktu_akhir', 
            'catatan', 
            'ruangan'
        )


class IzinKegiatanUnitKerjaSerializer(serializers.ModelSerializer):
    subkegiatan = PeminjamanRuanganUnitKerjaSerializer(many=True)
    
    class Meta:
        model = IzinKegiatan
        fields = ('id', 'nama_kegiatan', 'organisasi', 'user', 'status_perizinan_kegiatan', 'subkegiatan')

    def create(self, validated_data):
        subkegiatan_data = validated_data.pop('subkegiatan')
        izin_kegiatan = IzinKegiatan.objects.create(**validated_data)
        for subkegiatan in subkegiatan_data:
            PeminjamanRuangan.objects.create(izin_kegiatan=izin_kegiatan, **subkegiatan)
        return izin_kegiatan

class PeminjamanRuanganMahasiswaSerializer(serializers.ModelSerializer):
    subkegiatan = PeminjamanRuanganUnitKerjaSerializer(many=True)

    class Meta: 
        model = IzinKegiatan
        fields = ('id', 'nama_kegiatan', 'organisasi', 'user', 'status_perizinan_kegiatan', 'subkegiatan')

    def update(self,izin_kegiatan,validated_data):
        subkegiatan_data = validated_data.pop('subkegiatan')
        for subkegiatan in subkegiatan_data:
            PeminjamanRuangan.objects.create(izin_kegiatan=izin_kegiatan, **subkegiatan)
        return izin_kegiatan
     

