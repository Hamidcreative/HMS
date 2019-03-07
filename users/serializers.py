from rest_framework import serializers
from users.models import Profile, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



class UsersSerializer(serializers.ModelSerializer):   #  used to get user profile
    # user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','is_active')

class DoctorsSerializer(serializers.ModelSerializer):   #  used to get user profile
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = ('user_id','user','title', 'gender', 'designation', 'qualification', 'experience', 'primary_hospital', 'secondary_hospital', 'specialty', 'mobile_no', 'timing', 'avatar',
        'martial_status', 'weight', 'height', 'blood_type', 'notes', 'created_date', 'modified_date')


class StudentSerializer(serializers.ModelSerializer):   #  used to get user profile
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields = ('user_id','user','title', 'gender', 'mobile_no', 'avatar', 'martial_status', 'weight', 'height', 'blood_type', 'notes', 'created_date', 'modified_date')




