
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views
from django.conf.urls import url

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'students', views.StudentViewSet)
#router.register(r'doctors', views.DoctorsViewSet)

student_list = views.StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
student_detail = views.StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
u_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

doctor_list = views.DoctorsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
doctor_detail = views.DoctorsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
# The API URLs are now determined automatically by the router.
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('students', student_list, name='students'),
    path('doctors', doctor_list, name='doctors'),
    path('users', u_list, name='users'),
    path('users-list', views.users_listing, name='users_listing'),
    path('doctors-list', views.doctors_listing, name='doctors_listing'),
    path('student-list', views.student_listing, name='student_listing'),
    path('users-dashboard', views.users_dashboard, name='users_dashboard'),


])

