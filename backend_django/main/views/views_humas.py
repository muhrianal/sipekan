from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate

from ..models.profile import Profile
from django.contrib.auth.models import User


from rest_framework import status, permissions
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from ..permissions import AllowOnlyAdminFASTUR, AllowOnlyAdminHUMAS, AllowOnlyAdminPKM

# from ..models.peminjaman_ruangan import PeminjamanRuangan

# from ..models.peminjaman_ruangan import Ruangan

from ..models.humas import PerizinanPublikasi, PermintaanProtokoler, PermintaanSouvenir

from ..models.izin_kegiatan import IzinKegiatan

# from ..serializers.peminjaman_ruangan_serializer import PeminjamanRuanganSerializer

from ..serializers.humas_serializer import PermintaanSouvenirSeriliazer,PerizinanPublikasiSerializer,PermintaanProtokolerSerializer, PerizinanKegiatanSerializer

from django.http.response import JsonResponse

@api_view(['GET'])
@permission_classes([permissions.AllowAny,])
def list_perizinan_humas(request):

    if request.method == 'GET':
        list_perizinan_humas_kegiatan = IzinKegiatan.objects.all()
        list_perizinan_humas_kegiatan_serialized = PerizinanKegiatanSerializer(list_perizinan_humas_kegiatan,many=True)
        return JsonResponse(list_perizinan_humas_kegiatan_serialized.data, safe=False)
    
    #case for else
    data = {
        'message' : 'invalid API call'
    }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny,])
def get_post_perizinan_humas(request,id_izin_kegiatan):
    try: 
        izin_kegiatan =IzinKegiatan.objects.get(pk=id_izin_kegiatan)
    except:
        return JsonResponse({'message': 'Izin kegiatan tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        permintaan_data = JSONParser().parse(request)
        permintaan_humas_serialized = PerizinanKegiatanSerializer(izin_kegiatan, data = permintaan_data)
        if permintaan_humas_serialized.is_valid():
            permintaan_humas_serialized.save()
            return JsonResponse(permintaan_humas_serialized.data)
        return JsonResponse(permintaan_humas_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        detail_perizinan_humas_kegiatan_serialized = PerizinanKegiatanSerializer(izin_kegiatan)
        return JsonResponse(detail_perizinan_humas_kegiatan_serialized.data, safe=False)
    
    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['PUT'])
# @permission_classes([permissions.AllowAny,])
# def put_perizinan_humas(request,id_izin_kegiatan):
#     try: 
#         izin_kegiatan =IzinKegiatan.objects.get(pk=id_izin_kegiatan)
#     except:
#         return JsonResponse({'message': 'Izin kegiatan tidak ada'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         perizinan_data = JSONParser().parse(request)
     