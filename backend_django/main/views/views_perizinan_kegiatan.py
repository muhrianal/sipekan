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

from ..models.izin_kegiatan import IzinKegiatan

from ..models.izin_kegiatan import DetailKegiatan

from ..serializers.kalender_serializer import KalenderSerializer

from django.http.response import JsonResponse

@api_view(['GET'])
@permission_classes([permissions.AllowAny,])
def list_detail_kegiatan_kalender(request):

    if request.method == 'GET':
        list_detail_kegiatan = DetailKegiatan.objects.all()
        kalender_serialized = KalenderSerializer(list_detail_kegiatan, many=True)
        return JsonResponse(kalender_serialized.data, safe=False)
    
    #case for else
    data = {
        'message' : 'invalid API call'
    }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)