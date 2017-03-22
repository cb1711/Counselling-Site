from .models import Student,Counsellor,Appointment
from django.contrib.auth.models import User
from django import forms

class StudentForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model= User
		fields = ('username', 'email', 'password')
	
class StudentProfileForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=('Branch','Year','RollNumber','Mobile')

class CounsellorForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model= User
		fields = ('username', 'email', 'password')
	
class CounsellorProfileForm(forms.ModelForm):
	class Meta:
		model=Counsellor
		fields=('Type','Mobile')


