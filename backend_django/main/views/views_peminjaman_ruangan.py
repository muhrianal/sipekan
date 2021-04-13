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

from ..models.peminjaman_ruangan import PeminjamanRuangan

from ..models.peminjaman_ruangan import Ruangan

from ..serializers.peminjaman_ruangan_serializer import PeminjamanRuanganSerializer, RuanganSerializer

from django.http.response import JsonResponse

@api_view(['GET'])
@permission_classes([permissions.AllowAny,])
def list_peminjaman_ruangan(request):

    if request.method == 'GET':
        list_peminjaman_ruangan = PeminjamanRuangan.objects.all()
        peminjaman_ruangan_serialized = PeminjamanRuanganSerializer(list_peminjaman_ruangan, many=True)
        return JsonResponse(peminjaman_ruangan_serialized.data, safe=False)
    
    #case for else
    data = {
        'message' : 'invalid API call'
    }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny,])
def list_ruangan(request):
    if request.method == 'GET':
        daftar_ruangan = Ruangan.objects.all()
        ruangans_serialized = RuanganSerializer(daftar_ruangan, many= True)
        return JsonResponse(ruangans_serialized.data, safe=False)
#     data = {
#             'message' : 'invalid API call'
#         }
#     return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        ruang_data = JSONParser().parse(request)
        ruang_serializer = RuanganSerializer(data=ruang_data)
        if ruang_serializer.is_valid():
            ruang_serializer.save()
            return JsonResponse(ruang_serializer.data, status=status.HTTP_201_CREATED)
        data = {
                    'message' : 'invalid API call'
                }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes([permissions.AllowAny,])
def detail_ruangan(request,pk):
    try:
        ruangan = Ruangan.objects.get(pk=pk)
    except Ruangan.DoesNotExist:
        return JsonResponse({'message': 'Ruangan tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ruangan_serialized = RuanganSerializer(ruangan)
        return JsonResponse(ruangan_serialized.data,)
#     data = {
#             'message' : 'invalid API call'
#         }
#     return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
            ruangan_data = JSONParser().parse(request)
            ruangan_serializer = RuanganSerializer(ruangan, data=ruangan_data)
            if ruangan_serializer.is_valid():
                ruangan_serializer.save()
                return JsonResponse(ruangan_serializer.data)
            return JsonResponse(ruangan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ruangan.delete()
        return JsonResponse({'messagee': 'Ruangan berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)
#         #do something untuk request DELETE, misal hapus izin kegiatan yang sudah ada