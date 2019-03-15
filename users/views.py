from django.shortcuts import get_object_or_404, render
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Profile, Appointment
from hospital.models import Hospital
from users.serializers import UsersSerializer,DoctorsSerializer,StudentSerializer,AppointmentsSerializer,ProfileSerializer
from django.http import Http404, HttpResponse
from rest_framework import mixins
from rest_framework import generics
from users.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from datetime import date

from .forms import Doctorsform, UserCreationform,Studentform,Adminform
from default.utils import *
from default.templatetags.custom_tags import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id')

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        post_data = request.data['groups']
        user.groups.add(post_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #def update(self, request, pk=None):
    #    instance = self.queryset.get(pk=pk)
    #    serializer = self.serializer_class(instance, data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    serializer.save()
    #    post_data = request.data['groups']
    #    old_groups = instance.groups.exclude(id=pk)
    #    if old_groups:
    #        instance.groups.remove(*list(old_groups))
    #    instance.groups.add(post_data)
    #    #if not instance.groups.filter(id=pk):
    #    #    instance.groups.add(post_data)
    #
    #    headers = self.get_success_headers(serializer.data)
    #    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def users_listing(request):
    tokens = request.session.get('token')
    return render(request,'users/users.html',{'token': tokens,})

def add_user(request):
    form = UserCreationform()
    context = { 'form' : form, 'app':'users','type':'POST','app_url':'users','redirect':'users-list'}
    return render(request, 'users/add_user.html',context)

def edit_user(request, id):
    instance = get_object_or_404(User, id=id)
    form = UserCreationform(request.POST or None, instance=instance)
    group = instance.groups.values_list('name', flat=True).first()
    print(group)
    group_form  = ''
    if group == 'Doctor':
         group_form = Doctorsform(request.POST or None, instance=instance.profile)
    elif group == 'Student':
         group_form = Studentform(request.POST or None, instance=instance.profile)
    elif group == 'Pharmacist':
         group_form = Adminform(request.POST or None, instance=instance.profile)
    elif group == 'Hospital Admin':
         group_form = Adminform(request.POST or None, instance=instance.profile)
    elif group == 'Admin':
         group_form = Adminform(request.POST or None, instance=instance.profile)
    else:
         group_form = Adminform(request.POST or None, instance=instance.profile)

    context = {'form' : form,'group_form' : group_form, 'user':instance,'user_profile':instance.profile, 'app':'users','type':'PUT','app_url':'users' ,'group':group}
    return render(request,'users/add_user.html',context)

class DoctorsViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = DoctorsSerializer
    def perform_create(self, serializer):
       serializer.save()

def doctors_listing(request):
    tokens = request.session.get('token')
    return render(request,'users/doctors/doctors.html',{'token': tokens,})

def add_doctor(request):
    context = {'form' : Doctorsform,'app':'doctors','type':'POST','app_url':'doctors'}
    return render(request,'hospital/add_hospital.html',context)

def edit_doctor(request, user_id):
    instance = get_object_or_404(Profile, user_id=user_id)
    form = Doctorsform(request.POST or None, instance=instance)
    context = {'form' : form, 'obj':instance, 'app':'doctors','type':'PUT','app_url':'doctors'}
    return render(request,'hospital/add_hospital.html',context)

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)

def student_listing(request):
    tokens = request.session.get('token')
    return render(request,'users/students/studemts.html',{'token': tokens,})

class  AppointmentsViewSet(viewsets.ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentsSerializer

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)

def appointments_listing(request):
    tokens = request.session.get('token')
    return render(request,'users/appointments/appointments.html',{'token': tokens,})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users', request=request, format=format),
        'students': reverse('students', request=request, format=format),
        'doctors': reverse('doctors', request=request, format=format),
        'hospitals': reverse('hospitals', request=request, format=format),
    })

def users_dashboard(request):
    tokens = request.session.get('token')
    users = request.session.get('group')
    return render(request,'users/dashboard.html',{'token': tokens, 'username':users})


