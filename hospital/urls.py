
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hospital import views
from django.conf.urls import url

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'hospitals', views.HospitalsViewSet)

hospitals_list = views.HospitalsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
hospitals_detail = views.HospitalsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('hospitals', hospitals_list, name='hospitals'),
    path('hospitals-listing', views.hospitals, name='hospitals-listing'),
    ]