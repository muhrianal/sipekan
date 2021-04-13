from rest_framework import serializers 

from ..models.izin_kegiatan import DetailKegiatan

class KalenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailKegiatan
        fields = '__all__'