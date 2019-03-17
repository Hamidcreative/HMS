from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	title = models.CharField(max_length=100, blank=True, null=True)
	# first_name = models.CharField(max_length=100, blank=True, null=True)
	# last_name = models.CharField(max_length=100, blank=True, null=True)
	gender = models.CharField(max_length=15, blank=True, null=True)
	designation =  models.CharField(max_length=250, blank=True, null=True)
	qualification = models.CharField(max_length=250, blank=True, null=True)
	experience = models.CharField(max_length=250, blank=True, null=True)
	primary_hospital = models.ForeignKey("hospital.Hospital", on_delete=models.SET_NULL, blank=True, null=True)                                    
	secondary_hospital = models.ForeignKey("hospital.Hospital", on_delete=models.SET_NULL, related_name='secondary_hospital',blank=True, null=True)                                    
	specialty = models.CharField(max_length=250, blank=True, null=True)
	mobile_no = models.CharField(max_length=25, blank=True, null=True)
	timing = models.TextField(blank=True, null=True)
	avatar = models.CharField(max_length=250, blank=True, null=True)
	martial_status = models.CharField(max_length=250, blank=True, null=True)
	weight = models.CharField(max_length=250, blank=True, null=True)
	height = models.CharField(max_length=250, blank=True, null=True)
	diseases  = models.CharField(max_length=250, blank=True, null=True)
	allergies = models.CharField(max_length=250, blank=True, null=True)
	blood_type = models.CharField(max_length=250, blank=True, null=True)
	notes = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
	    ordering = ('created_date',)

	def __str__(self): # converting obj
                return f'{self.user.username} Profile'


class Appointment(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')    
	doctor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='doctor', blank=True, null=True)
	datetime = models.DateTimeField()
	disease = models.TextField()
	notes = models.TextField(blank=True, null=True)
	status = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	def __str__(self): # converting obj
	    return f'{self.student.username} appointment with {self.doctor.username}'


class Prescription(models.Model):
	appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  
	how_to_use = models.TextField(blank=True, null=True)
	medicine_name = models.CharField(max_length=250, blank=True, null=True)
	medicine_type = models.ForeignKey("hospital.MedicineType", on_delete=models.SET_NULL, blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	
