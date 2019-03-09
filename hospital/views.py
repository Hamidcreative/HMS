from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from users.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions

class HospitalsViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    def perform_create(self, serializer):
        serializer.save()

def hospitals(request):
    return render(request,'hospital/hospital.html')





