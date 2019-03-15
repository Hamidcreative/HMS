
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from users import views
from django.conf.urls import url

urlpatterns = format_suffix_patterns([
    path('appointments-list', views.appointments_listing, name='appointments_listing'),
    path('users-list', views.users_listing, name='users_listing'),
    path('users/add', views.add_user, name='add_user'),
    path('users/<int:id>/', views.edit_user, name='edit_user'),
    path('doctors-list', views.doctors_listing, name='doctors_listing'),
    #path('doctors/add', views.add_doctor, name='add_doctor'),
    #path('doctors/<int:id>/', views.edit_doctor, name='edit_doctor'),
    path('student-list', views.student_listing, name='student_listing'),
    path('users-dashboard', views.users_dashboard, name='users_dashboard'),
])

