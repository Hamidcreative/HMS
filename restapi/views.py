from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.core import serializers
import json

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def login(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        if request.data.get("next") == '/users-dashboard':
            serialized_obj = serializers.serialize('json', [ user, ])

            #user = { 'user_name':user.username, 'first_name':user.first_name,'last_name':user.last_name,'email':user.email, 'group':user.groups.values_list('name',flat=True)}

            request.session['token'] = token.key
            request.session['username'] = user.username
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            request.session['group'] = user.groups.values_list('name',flat=True)[0]
            return redirect('users_dashboard')
        else:
           serialized_obj = serializers.serialize('json', [ user, ])
           user = { 'user_name':user.username, 'first_name':user.first_name,'last_name':user.last_name,'email':user.email, 'group':user.groups.values_list('name',flat=True)}
           #profile = { 'title':user.profile.title, 'gender':user.profile.gender,'last_name':user.last_name,'email':user.email, 'group':user.groups.values_list('name',flat=True)}
           #profile = {}
           #user = dict(users.items() | profile.items())

           return Response({'token': token.key, 'user':user},status=HTTP_200_OK)
    else:
        return render(request,'users/login.html',{'next': 'users_dashboard',})

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)