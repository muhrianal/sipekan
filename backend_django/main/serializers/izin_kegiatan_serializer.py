from rest_framework import serializers

from ..models.izin_kegiatan import IzinKegiatan
from ..models.izin_kegiatan import DetailKegiatan
from ..models.peminjaman_ruangan import PeminjamanRuangan
from ..models.humas import PermintaanProtokoler, PerizinanPublikasi, PermintaanSouvenir

class PeminjamanRuanganSerializer(serializers.ModelSerializer):


    class Meta:
        model = PeminjamanRuangan
        fields = '__all__'

class PermintaanProtokolerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PermintaanProtokoler
        fields = '__all__'

class PerizinanPublikasiSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerizinanPublikasi
        fields = '__all__'

class PermintaanSouvenirSerializer(serializers.ModelSerializer):

    class Meta:
        model = PermintaanSouvenir
        fields = '__all__'


class IzinKegiatanSerializer(serializers.ModelSerializer):

    peminjaman_ruangan = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    permintaan_protokoler = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    perizinan_publikasi = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    permintaan_souvenir = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = IzinKegiatan
        fields = '__all__'



# class TestSerializer(serializers.Serializer):
#     nested1 = IzinKegiatanSerializer(source='*')
#     nested2 = PeminjamanRuanganSerializer(source='*')
#
# data = {
#     'nested1': {IzinKegiatan},
#     'nested2': {PeminjamanRuangan}
#     }
# serializer = TestSerializer(data=data)
# assert serializer.is_valid()

# assert.serializer.validated_data == {
#
#
# }

class DetailKegiatanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailKegiatan
        fields = '__all__'