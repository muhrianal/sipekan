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

from django.http.response import JsonResponse
from ..models.izin_kegiatan import IzinKegiatan, DetailKegiatan
from ..serializers.izin_kegiatan_serializer import IzinKegiatanMahasiswaSerializer
from django.http.response import JsonResponse

@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny,]) #nanti diganti jadi mahasiswa
def get_post_izin_kegiatan_mahasiswa(request):
    if request.method == 'POST':
        perizinan_data = JSONParser().parse(request)
        perizinan_data_serialized = IzinKegiatanMahasiswaSerializer(data=perizinan_data)
        if perizinan_data_serialized.is_valid():
            perizinan_data_serialized.save()
            return JsonResponse(perizinan_data_serialized.data,status=status.HTTP_201_CREATED)
        return JsonResponse(perizinan_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        list_izin_kegiatan_mahasiwa = IzinKegiatan.objects.all()
        list_izin_kegiatan_mahasiwa_serialized = IzinKegiatanMahasiswaSerializer(list_izin_kegiatan_mahasiwa, many=True)
        return JsonResponse(list_izin_kegiatan_mahasiwa_serialized.data, safe=False)
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        


