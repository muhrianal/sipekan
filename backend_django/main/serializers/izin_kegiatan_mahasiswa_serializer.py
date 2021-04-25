from rest_framework import serializers 

from ..models.izin_kegiatan import IzinKegiatan, DetailKegiatan

class DetailKegiatanMahasiswaSerializer(serializers.ModelSerializer):
    
    class Meta:    
        model = DetailKegiatan
        # fields = '__all__'
        fields =(
            'id',
            'waktu_tanggal_mulai',
            'waktu_tanggal_akhir',
            'email_pic',
            'nama_pic',
            'hp_pic',
            'npm_pic',
            'npm_ketua_organisasi',
            'nama_ketua_organisasi',
            'tempat_pelaksanaan',
            'sumber_pendanaan',
            'alasan_penolakan',
            'file_info_kegiatan',
            'created_at', 
            'updated_at', 
        )

class IzinKegiatanMahasiswaSerializer(serializers.ModelSerializer):
    detail_kegiatan = DetailKegiatanMahasiswaSerializer()
    
    class Meta:
        model = IzinKegiatan
        fields = ('id','nama_kegiatan', 'organisasi', 'user', 'status_perizinan_kegiatan','detail_kegiatan')

    def create(self, validated_data):
        detail_kegiatan_data = validated_data.pop('detail_kegiatan')
        izin_kegiatan = IzinKegiatan.objects.create(**validated_data)
        DetailKegiatan.objects.create(izin_kegiatan = izin_kegiatan, **detail_kegiatan_data)
        return izin_kegiatan

        
