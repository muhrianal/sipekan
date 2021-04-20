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





