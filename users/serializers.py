from rest_framework import serializers
from users.models import Profile, Appointment
from django.contrib.auth.models import User ,Group
from django.contrib.auth.hashers import make_password


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name',)

class UsersSerializer(serializers.ModelSerializer):   #  used to get user profile
    groups = GroupSerializer(many=True, read_only=True)
    id = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        # update password
        password = request.data['password1']
        user = super(UsersSerializer, self).update(instance, validated_data)
        if password: 
            user.set_password(password)
        user.save()

        # update user group
        group = request.data['groups']
        # check if group not exist already
        if not user.groups.filter(id=group):
            user.groups.add(group)

        old_groups = user.groups.exclude(id=group)
        if old_groups:
            user.groups.remove(*list(old_groups))
        return user

    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name','email','is_active','groups')
        datatables_always_serialize = ('id',)


class ProfileSerializer(serializers.ModelSerializer):   #  used to get user profile
    class Meta:
        model = Profile
        fields = ('user','gender', 'designation', 'qualification', 'experience', 'primary_hospital', 'secondary_hospital', 'specialty', 'mobile_no', 'timing', 'avatar',
        'martial_status', 'weight', 'height', 'blood_type', 'notes', 'created_date', 'modified_date')

class DoctorsSerializer(serializers.ModelSerializer):   #  used to get user profile
    user = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    is_active=serializers.CharField(source='user.is_active', read_only=True)
    class Meta:
        model = Profile
        fields = ('user_id','user','title','last_name','first_name','email', 'is_active', 'gender', 'designation', 'qualification', 'experience', 'primary_hospital', 'secondary_hospital', 'specialty', 'mobile_no', 'timing', 'avatar',
        'martial_status', 'weight', 'height', 'blood_type', 'notes', 'created_date', 'modified_date')


class StudentSerializer(serializers.ModelSerializer):   #  used to get user profile
    user = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    is_active=serializers.CharField(source='user.is_active', read_only=True)

    class Meta:
        model = Profile
        fields = ('user_id','user','title','email', 'is_active', 'first_name','last_name', 'gender', 'mobile_no', 'avatar', 'martial_status', 'weight', 'height', 'blood_type', 'notes', 'created_date', 'modified_date')

class AppointmentsSerializer(serializers.ModelSerializer):   #  used to get user Appointments
    student = serializers.CharField(source='student.username', read_only=True)
    doctor  = serializers.CharField(source='doctor.username', read_only=True)

    class Meta:
        model = Appointment
        fields = ('id','student','doctor','datetime','disease', 'notes', 'status','created_date', 'modified_date')




