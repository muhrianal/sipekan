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

    # def create(self, validated_data):
    #     id_izin_kegiatan = validated_data.pop('id_izin_kegiatain')

    #     izin_kegiatan = IzinKegiatan.objects.get(pk=id_izin_kegiatan)

    #     permintaan_protokoler = validated_data.pop('permintaan_protokoler')
    #     permintaan_souvenir = validated_data.pop('permintaan_souvenir')
    #     perizininan_publikasi  = validated_data.pop('perizinan_publikasi')
        
    #     for minta_protokoler in permintaan_protokoler:
    #         PermintaanProtokoler.objects.create(izin_kegiatan=izin_kegiatan, **minta_protokoler)

    #     #do the same thing (with loop) buat permintaan souvenir dan perizinan publikasi