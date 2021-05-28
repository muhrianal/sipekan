from rest_framework import serializers 

from ..models.humas import PerizinanPublikasi,PermintaanSouvenir,PermintaanProtokoler, JenisPublikasi, Souvenir, JenisIzinPublikasi

from ..models.izin_kegiatan import IzinKegiatan

from .peminjaman_ruangan_serializer import UserSerializer

class SouvenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = ('id', 'nama_souvenir','region','kelas', 'stok')

class JenisPublikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisPublikasi
        fields = '__all__'

class JenisIzinPublikasiSerializer(serializers.ModelSerializer):
    jenis_publikasi = JenisPublikasiSerializer(read_only = True)
    class Meta:
        model = JenisIzinPublikasi
        fields = '__all__'
 
class PerizinanPublikasiSerializer(serializers.ModelSerializer):
    jenis_izin_publikasi= JenisIzinPublikasiSerializer( many=True)
    class Meta:
        model = PerizinanPublikasi
        fields = ('id','tanggal_mulai', 'tanggal_akhir', 'jenis_izin_publikasi','keterangan', 'file_materi_kegiatan', 'file_flyer_pengumuman','izin_kegiatan')
    
    def create(self,validated_data):
        print(validated_data)
        jenis_izin_publikasi_data = validated_data.pop('jenis_izin_publikasi')
        perizinan_publikasi = PerizinanPublikasi.objects.create(**validated_data)
        for jenis_izin in jenis_izin_publikasi_data:
            JenisIzinPublikasi.objects.create(perizinan_publikasi=perizinan_publikasi, **jenis_izin)
        return perizinan_publikasi        

class PermintaanSouvenirHumasSerializer(serializers.ModelSerializer):
    souvenir = SouvenirSerializer(read_only=True)
    class Meta:
        model = PermintaanSouvenir
        fields =  fields = ('id','alasan_penolakan', 'status_permintaan_souvenir', 'jumlah', 'souvenir', 
        'nama_penerima_souvenir', 'kelas_penerima_souvenir', 'region_penerima_souvenir', 'jabatan_penerima_souvenir','created_at','updated_at' )

class PermintaanSouvenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermintaanSouvenir
        fields = ('id','alasan_penolakan', 'status_permintaan_souvenir', 'jumlah', 'souvenir', 
        'nama_penerima_souvenir', 'kelas_penerima_souvenir', 'region_penerima_souvenir', 'jabatan_penerima_souvenir' )

class PermintaanProtokolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermintaanProtokoler
        fields = ('id','deskripsi_kebutuhan','status_permintaan_protokoler','alasan_penolakan','created_at','updated_at')

class PerizinanKegiatanSerializer(serializers.ModelSerializer):
    permintaan_protokoler = PermintaanProtokolerSerializer(required = False)
    permintaan_souvenir = PermintaanSouvenirSerializer(many=True, required= False)
    
    class Meta:
        model = IzinKegiatan
        fields = ('id', 'permintaan_souvenir', 'permintaan_protokoler')
    
    def update(self, izin_kegiatan, validated_data):
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

class  IzinKegiatanHumasSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    perizinan_publikasi = PerizinanPublikasiSerializer(required=False)
    permintaan_protokoler = PermintaanProtokolerSerializer(required = False)
    permintaan_souvenir =PermintaanSouvenirHumasSerializer(many=True, required= False)

    class Meta:
        model = IzinKegiatan
        fields = ('id','nama_kegiatan', 'organisasi', 'status_perizinan_kegiatan', 'user','perizinan_publikasi','permintaan_souvenir', 'permintaan_protokoler')



    

