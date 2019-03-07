from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Profile
from users.serializers import UsersSerializer,DoctorsSerializer,StudentSerializer
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from users.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save()










class DoctorsViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = DoctorsSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('Userlist', request=request, format=format),
    })

def users_listing(request):
    return render(request,'users/users.html')

def users_dashboard(request):
    return render(request,'users/dashboard.html')


