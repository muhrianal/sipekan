from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate

from ..models.profile import Profile
from ..models.peminjaman_ruangan import Ruangan
from django.contrib.auth.models import User

from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from ..serializers.peminjaman_ruangan_serializer import RuanganSerializer





@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([permissions.AllowAny,])
def ruangan_list(request):
    if request.method == 'GET':
        daftar_ruangan = Ruangan.objects.all()
        ruangan_serializer = RuanganSerializer(ruangan_list, many= True)
        return JsonResponse(ruangan_serializer.data, safe=False)

    elif request.method == 'POST':
        ruang_data = JSONParser().parse(request)
        ruang_serializer = RuanganSerializer(data=ruang_data)
        if ruang_serializer.is_valid():
            ruang_serializer.save()
            return JsonResponse(ruang_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ruang_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #do something untuk request POST, misal bikin izin kegiatan baru
    elif request.method == 'DELETE':
        count = Ruangan.objects.all().delete()
        return JsonResponse({'messagee': '{} Ruangan berhasil dihapus'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        #do something untuk request DELETE, misal hapus izin kegiatan yang sudah ada