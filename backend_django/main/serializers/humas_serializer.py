from rest_framework import serializers 

from ..models.humas import PerizinanPublikasi,PermintaanSouvenir,PermintaanProtokoler, JenisPublikasi, Souvenir

from ..models.izin_kegiatan import IzinKegiatan

class JenisPublikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisPublikasi
        fields = '__all__'

class PerizinanPublikasiSerializer(serializers.ModelSerializer):
    jenis_publikasi = JenisPublikasiSerializer(read_only = True, many = True)
    class Meta:
        model = PerizinanPublikasi
        # fields = '__all__'
        fields = ('id','tanggal_mulai', 'tanggal_akhir', 'jenis_publikasi', 'status_perizinan_publikasi', 'alasan_penolakan','keterangan', 'file_materi_kegiatan', 'file_flyer_pengumuman')

class PermintaanSouvenirSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = PermintaanSouvenir
        # fields = '__all__'
        fields = ('id','alasan_penolakan', 'status_permintaan_souvenir', 'jumlah', 'souvenir', 
        'nama_penerima_souvenir', 'jabatan_penerima_souvenir', )

class PermintaanProtokolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermintaanProtokoler
        # fields = '__all__'
        fields = ('id','deskripsi_kebutuhan')

class PerizinanKegiatanSerializer(serializers.ModelSerializer):
    perizinan_publikasi = PerizinanPublikasiSerializer(required = False)
    permintaan_protokoler = PermintaanProtokolerSerializer(required = False)
    permintaan_souvenir = PermintaanSouvenirSeriliazer(many=True, required= False)
    
    class Meta:
        model = IzinKegiatan
        fields = ('id', 'nama_kegiatan', 'organisasi', 'user', 'status_perizinan_kegiatan', 
        'perizinan_publikasi', 'permintaan_souvenir', 'permintaan_protokoler')
    
    def update(self, izin_kegiatan, validated_data):
        # publikasi
        if 'perizinan_publikasi' in validated_data:
            perizinan_publikasi = validated_data.pop('perizinan_publikasi')
            PerizinanPublikasi.objects.create(izin_kegiatan=izin_kegiatan, **perizinan_publikasi)

        #protokoler
        if 'permintaan_protokoler' in validated_data:
            permintaan_protokoler= validated_data.pop('permintaan_protokoler')
            PermintaanProtokoler.objects.create(izin_kegiatan=izin_kegiatan, **permintaan_protokoler)

        # souvenir
        if 'permintaan_souvenir' in validated_data:
            permintaan_souvenir_data = validated_data.pop('permintaan_souvenir')
            for permintaan_souvenir in permintaan_souvenir_data:
                PermintaanSouvenir.objects.create(izin_kegiatan=izin_kegiatan, **permintaan_souvenir)
        
        return izin_kegiatan    

class SouvenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = '__all__'

    

