from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status, permissions
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from ..permissions import AllowOnlyAdminFASTUR, AllowOnlyAdminHUMAS, AllowOnlyAdminPKM
from ..models.profile import Profile
from ..models.peminjaman_ruangan import PeminjamanRuangan
from ..models.peminjaman_ruangan import Ruangan
from ..models.izin_kegiatan import IzinKegiatan
from ..serializers.peminjaman_ruangan_serializer import PeminjamanRuanganUnitKerjaSerializer, IzinKegiatanUnitKerjaSerializer, PeminjamanRuanganMahasiswaSerializer
from django.http.response import JsonResponse


@api_view(['PUT',])
@permission_classes([permissions.AllowAny,]) #nanti diganti jadi admin fastur dan peminjam
def update_peminjaman_ruangan_by_id_peminjaman_ruangan(request, id_peminjaman):
    try:
        peminjaman_ruangan = PeminjamanRuangan.objects.get(pk=id_peminjaman)
    except:
        return JsonResponse({'message': 'Peminjaman ruangan tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

        peminjaman_data = JSONParser().parse(request) 
        peminjaman_ruangan_serialized = PeminjamanRuanganUnitKerjaSerializer(peminjaman_ruangan, data=peminjaman_data)
        
        if peminjaman_ruangan_serialized.is_valid():
            peminjaman_ruangan_serialized.save()
            return JsonResponse(peminjaman_ruangan_serialized.data)

        return JsonResponse(peminjaman_ruangan_serialized.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
 
@api_view(['POST','GET'])
@permission_classes([permissions.AllowAny,]) #nanti diganti jadi unit kerja
def get_post_peminjaman_ruangan_unit_kerja(request):
    if request.method == 'POST':
        peminjaman_data = JSONParser().parse(request)
        peminjaman_data_serialized = IzinKegiatanUnitKerjaSerializer(data=peminjaman_data)
        if peminjaman_data_serialized.is_valid():
            peminjaman_data_serialized.save()
            return JsonResponse(peminjaman_data_serialized.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(peminjaman_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        list_izin_kegiatan = IzinKegiatan.objects.all()
        list_izin_kegiatan_serialized = IzinKegiatanUnitKerjaSerializer(list_izin_kegiatan, many=True)
        return JsonResponse(list_izin_kegiatan_serialized.data, safe=False)

    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def post_peminjaman_ruangan_mahasiswa(request, id_izin_kegiatan):
    try: 
        izin_kegiatan =IzinKegiatan.objects.get(pk=id_izin_kegiatan)
    except:
        return JsonResponse({'message': 'Izin kegiatan tidak ada'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        peminjaman_data = JSONParser().parse(request)
        peminjaman_ruangan_serialized =PeminjamanRuanganMahasiswaSerializer(izin_kegiatan,data=peminjaman_data)
        if peminjaman_ruangan_serialized.is_valid():
            peminjaman_ruangan_serialized.save()
            return JsonResponse(peminjaman_ruangan_serialized.data)
        return JsonResponse(peminjaman_ruangan_serialized.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)