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

from ..models.humas import PerizinanPublikasi, PermintaanProtokoler, PermintaanSouvenir, JenisPublikasi, Souvenir

from ..models.izin_kegiatan import IzinKegiatan

from ..serializers.humas_serializer import PermintaanSouvenirSeriliazer,PerizinanPublikasiSerializer,PermintaanProtokolerSerializer, PerizinanKegiatanSerializer, JenisPublikasiSerializer,SouvenirSerializer,PerizinanPublikasiSerializer

from django.http.response import JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

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
            return JsonResponse(permintaan_humas_serialized.data,safe=False)
        return JsonResponse(permintaan_humas_serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        detail_perizinan_humas_kegiatan_serialized = PerizinanKegiatanSerializer(izin_kegiatan)
        return JsonResponse(detail_perizinan_humas_kegiatan_serialized.data, safe=False)
    
    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny,]) 
@parser_classes([MultiPartParser, FormParser])
def post_perizinan_publikasi(request):
    if request.method == 'POST': # post detail izin kegiatan
        perizinan_data_serialized = PerizinanPublikasiSerializer(data=request.data)
        if perizinan_data_serialized.is_valid():
            perizinan_data_serialized.save()
            return JsonResponse(perizinan_data_serialized.data,status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(perizinan_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) #nanti diganti jadi mahasiswa dan unit kerja
def get_jenis_publikasi(request):
    if request.method == 'GET':
        list_jenis_publikasi = JenisPublikasi.objects.all()
        list_jenis_publikasi_serialized = JenisPublikasiSerializer(list_jenis_publikasi, many=True)
        return JsonResponse(list_jenis_publikasi_serialized.data,safe=False)
    
    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes([permissions.AllowAny,]) #nanti diganti jadi mahasiswa dan unit kerja
def get_list_souvenir(request):
    if request.method == 'GET':
        list_souvenir = Souvenir.objects.all()
        list_souvenir_serialized = SouvenirSerializer(list_souvenir, many=True)
        return JsonResponse(list_souvenir_serialized.data,safe=False)

    
    #case for else

    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def post_souvenir(request):
    if request.method == 'POST':
        souvenir_data = JSONParser().parse(request)
        souvenir_serializer = SouvenirSerializer(data=souvenir_data)
        if souvenir_serializer.is_valid():
            souvenir_serializer.save()
            return JsonResponse(souvenir_serializer.data, status=status.HTTP_201_CREATED)
        data = {
                    'message' : 'invalid API call'
                }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([permissions.AllowAny,])
def detail_souvenir(request,pk):
    try:
        souvenir = Souvenir.objects.get(pk=pk)
    except Souvenir.DoesNotExist:
        return JsonResponse({'message': 'Souvenir tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        souvenir_serialized = SouvenirSerializer(souvenir)
        return JsonResponse(souvenir_serialized.data, safe=False)
#     data = {
#             'message' : 'invalid API call'
#         }
#     return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
            souvenir_data = JSONParser().parse(request)
            souvenir_serializer = SouvenirSerializer(souvenir, data=souvenir_data)
            if souvenir_serializer.is_valid():
                souvenir_serializer.save()
                return JsonResponse(souvenir_serializer.data)
            return JsonResponse(souvenir_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        souvenir.delete()
        return JsonResponse({'message': 'Souvenir berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)
#         #do something untuk request DELETE, misal hapus izin kegiatan yang sudah ada
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['GET','PUT'])
@permission_classes([permissions.AllowAny,])
def detail_permintaan_protokoler(request,pk):
    try:
        permintaan_protokoler = PermintaanProtokoler.objects.get(pk=pk)
    except PermintaanProtokoler.DoesNotExist:
        return JsonResponse({'message': 'Permintaan protokoler tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        permintaan_protokoler_serialized = PermintaanProtokolerSerializer(permintaan_protokoler)
        return JsonResponse(permintaan_protokoler_serialized.data, safe=False)
    # data = {
    #         'message' : 'invalid API call'
    #     }
    elif request.method == 'PUT':
            permintaan_protokoler_data = JSONParser().parse(request)
            permintaan_protokoler_serializer = PermintaanProtokolerSerializer(permintaan_protokoler, data=permintaan_protokoler_data)
            if permintaan_protokoler_serializer.is_valid():
                permintaan_protokoler_serializer.save()
                return JsonResponse(permintaan_protokoler_serializer.data)
            return JsonResponse(permintaan_protokoler_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         #do something untuk request DELETE, misal hapus izin kegiatan yang sudah ada
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['GET','PUT'])
@permission_classes([permissions.AllowAny,])
def detail_permintaan_souvenir(request,pk):
    try:
        permintaan_souvenir = PermintaanSouvenir.objects.get(pk=pk)
    except PermintaanSouvenir.DoesNotExist:
        return JsonResponse({'message': 'Ruangan tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        permintaan_souvenir_serialized = PermintaanSouvenirSeriliazer(permintaan_souvenir)
        return JsonResponse(permintaan_souvenir_serialized.data, safe=False)
    elif request.method == 'PUT':
        permintaan_souvenir_data = JSONParser().parse(request)
        permintaan_souvenir_serializer = PermintaanSouvenirSeriliazer(permintaan_souvenir, data=permintaan_souvenir_data)
        if permintaan_souvenir_serializer.is_valid():
            permintaan_souvenir_serializer.save()
            return JsonResponse(permintaan_souvenir_serializer.data)
        return JsonResponse(permintaan_souvenir_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 