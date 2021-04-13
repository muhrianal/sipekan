from rest_framework import serializers 

from ..models.peminjaman_ruangan import PeminjamanRuangan

class KalenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeminjamanRuangan
        fields = '__all__'