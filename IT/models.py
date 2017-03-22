from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
	YEARS = (("2012", "2012"),("2013","2013"),("2014","2014"),("2015","2015"),("2016","2016"))	
	student=models.OneToOneField(User)
	Branch=models.CharField(max_length=30)
	Year=models.CharField( max_length=4,choices=YEARS)
	RollNumber=models.CharField(max_length=10)
	Mobile=models.CharField(max_length=10)
	
	def __unicode__(self):
                return self.student.username
	
			

class Counsellor(models.Model):
	types=(("Emotional","Emotional"),("Academic","Academic"))	
	counsellor=models.OneToOneField(User)
	Type=models.CharField(max_length=30,choices=types)
	Mobile=models.CharField(max_length=10)
	def __unicode__(self):
                return self.counsellor.username

class Appointment(models.Model):
	slots= (("4","4"),("4.5","4.5"),("5","5"),("5.5","5.5"))
	Student=models.ForeignKey(User,on_delete=models.CASCADE)
	Counsellor=models.ForeignKey(Counsellor,on_delete=models.CASCADE)
	Date=models.DateField()
	Time=models.CharField(max_length=4,choices=slots)
	def __unicode__(self):
		return str(self.Student)+":"+str(self.Counsellor.counsellor)

class Feedback(models.Model):
	Serial=models.AutoField(primary_key=True)
	Student=models.ForeignKey(User,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=200)
	Date=models.DateField()
	Time=models.TimeField()
	def __str__(self):
		return str(self.feedback)

class News(models.Model):
	Content=models.CharField(max_length=300)
	Date=models.DateField()
	Time=models.TimeField()
	Serial=models.AutoField(primary_key=True)
	def __str__(self):
		return self.Content

class Message(models.Model):
	Text=models.CharField(max_length=200)
	Date=models.DateField()
	Time=models.TimeField()
	Sender=models.ForeignKey(User,related_name="sender")
	Receiver=models.ForeignKey(User,related_name="receiver")
	Email=models.CharField(max_length=50,default="example@counsel.com")	
	def __unicode__(self):
		return str(self.Sender)+self.Text

