from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class Doctorsform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','gender', 'designation', 'qualification', 'experience', 'primary_hospital', 'secondary_hospital', 'specialty', 'mobile_no', 'timing', 'avatar',
				'martial_status', 'weight', 'height', 'blood_type', 'notes')

class Studentform(forms.ModelForm):
    class Meta:
        model  = Profile
        fields =('gender', 'mobile_no', 'avatar', 'martial_status', 'weight', 'height', 'blood_type','diseases','allergies','notes')

class Adminform(forms.ModelForm):
    class Meta:
        model  = Profile
        fields =('first_name','last_name','gender', 'mobile_no', 'avatar')


class UserCreationform(UserCreationForm):
    email = forms.EmailField()
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=True, initial=0)
    class Meta:
        model  = User
        fields = ['username','email','password1','password2','groups']

