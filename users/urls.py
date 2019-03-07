#from django.urls import path, url
#from rest_framework.urlpatterns import format_suffix_patterns
#from users import views
#
#
#
#
#
#from users.views import UserViewSet, api_root
#from rest_framework import renderers
#
#Userlist = UserViewSet.as_view({
#    'get': 'list',
#    'post': 'create',
#
#})
#User_detail = UserViewSet.as_view({
#    'get': 'retrieve',
#    'put': 'update',
#    'patch': 'partial_update',
#    'delete': 'destroy'
#})
#
#urlpatterns = format_suffix_patterns([
#    path('', api_root),
#    path('users/', Userlist, name='Userlist'),
#    path('users/<int:pk>/', User_detail, name='User_detail'),
#])

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views
from django.conf.urls import url

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'doctors', views.DoctorsViewSet)
router.register(r'students', views.StudentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('users-list', views.users_listing, name='users_listing'),
    path('users-dashboard', views.users_dashboard, name='users_dashboard'),

]