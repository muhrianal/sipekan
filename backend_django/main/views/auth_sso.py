from rest_framework import status, permissions
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from ..sso.decorators import with_sso_ui
from .utils_sso import process_sso_profile



@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
@with_sso_ui(force_login=False)
def login_with_sso(request, sso_profile):

    if sso_profile is not None:
        token = process_sso_profile(sso_profile)
        username = sso_profile['username']

        data = {
            'username' : username,
            'token' : token,
            'role' : 1
        }

        return Response(data=data, status=status.HTTP_200_OK)

    data = {'message': 'invalid sso'}
    return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    
