from django.db import models

# Create your models here.

class Hospital(models.Model):
	description = models.CharField(max_length=250)
	status = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.description) 
		
	class Meta:
		ordering = ['description']

class MedicineType(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=250, blank=True, null=True)
	status = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.description) 
		
	class Meta:
		ordering = ['name']