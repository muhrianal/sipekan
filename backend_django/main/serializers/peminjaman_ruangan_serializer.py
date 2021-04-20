from rest_framework import serializers 

from ..models.peminjaman_ruangan import PeminjamanRuangan
from ..models.peminjaman_ruangan import Ruangan

class PeminjamanRuanganSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeminjamanRuangan
        fields = '__all__'



class RuanganSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ruangan
        fields = '__all__'