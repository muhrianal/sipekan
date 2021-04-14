from rest_framework import serializers 

from ..models.izin_kegiatan import IzinKegiatan

class IzinKegiatanSerializer(serializers.ModelSerializer):

    class Meta:
        model = IzinKegiatan
        fields = '__all__'