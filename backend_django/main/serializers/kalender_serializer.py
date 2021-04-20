from rest_framework import serializers 

from ..models.peminjaman_ruangan import PeminjamanRuangan

class KalenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeminjamanRuangan
        fields = ('judul_peminjaman', 'ruangan', 'waktu_mulai', 'waktu_akhir')