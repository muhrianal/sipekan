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

from ..models.izin_kegiatan import DetailKegiatan, IzinKegiatan

from ..serializers.izin_kegiatan_serializer import IzinKegiatanSerializerSimplified, IzinKegiatanSerializer


from django.http.response import JsonResponse


@api_view(['PUT',])
@permission_classes([permissions.AllowAny,])
def update_izin_kegiatan_by_id_perizinan(request, id_perizinan):
    try:
        izin_kegiatan = IzinKegiatan.objects.get(pk=id_perizinan)
    except:
        return JsonResponse({'message': 'Izin kegiatan tidak ada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

        izin_data = JSONParser().parse(request) 
        izin_kegiatan_serialized = IzinKegiatanSerializerSimplified(izin_kegiatan, data=izin_data)
        
        if izin_kegiatan_serialized.is_valid():
            izin_kegiatan_serialized.save()
            return JsonResponse(izin_kegiatan_serialized.data)

        return JsonResponse(izin_kegiatan_serialized.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    #case for else
    return JsonResponse({'message' : 'invalid API method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['POST','GET'])
@permission_classes([permissions.AllowAny,])
def list_izin_kegiatan(request):

    if request.method == 'POST':
        izin_data = JSONParser().parse(request)
        izin_kegiatan_serialized = IzinKegiatanSerializerSimplified(data=izin_data)
        if peminjaman_data_serialized.is_valid():
            izin_kegiatan_serialized.save()
            return JsonResponse( izin_kegiatan_serialized.data, status=status.HTTP_201_CREATED) 
        return JsonResponse( izin_kegiatan_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        list_izin_kegiatan = IzinKegiatan.objects.all()
        izin_kegiatan_serialized = IzinKegiatanSerializer(list_izin_kegiatan, many=True)
        return JsonResponse(izin_kegiatan_serialized.data, safe=False)
    
    #case for else
    data = {
        'message' : 'invalid API call'
    }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
