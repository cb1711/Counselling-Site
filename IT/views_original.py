from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404,render_to_response
from django.views import generic
from .models import News,Student,Counsellor,Appointment,Feedback
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import StudentForm,StudentProfileForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.context_processors import auth
from django.db import connection
import datetime
import smtplib


from email.mime.text import MIMEText


def home(request):
	return render(request,'home.html')
def newstudents(request):
	return render(request,'newstudents_ug.html')
def map(request):
	return render(request,'map.html')
@login_required
def appointment(request):
	booked=False
	rejected=False
	if request.method=='POST':
		time=request.POST['time']
		tpe=request.POST['type']
		date=str(request.POST['date'])	
		li=Counsellor.objects.filter(Type=tpe)
		req=[]
		
		for i in li:
			
			with connection.cursor() as cursor:
				cursor.execute('select Counsellor_ID from IT_appointment where Date=%r and Counsellor_id=%d and Time=%s'%(date,i.id,time))
				row=cursor.fetchone()	
			
				
			if row is None:
				req.append(i)
				
				
				
		if req:
			appt=Appointment(Counsellor=req[0],Date=date,Time=time,Student=auth(request)['user'])
			appt.save()
			booked=True
			
		else:
			rejected=True
				
			
			
	return render(request,'appointment.html',{'booked':booked,'rejected':rejected})


def importantinfo(request):
	li=News.objects.raw('SELECT Serial,Content from IT_news')
	
	return render(request,'Importantinfo.html',{'newslist':li})
@login_required
def chat(request):
	curr_user=auth(request)['user']
	a=Student.objects.filter(student=curr_user)
	profile=[]
	slot="0"
	now = datetime.datetime.now()
	today4pm =now.replace(hour=16, minute=0, second=0, microsecond=0)
	today45pm =now.replace(hour=16, minute=30, second=0, microsecond=0)
	today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
	today55pm = now.replace(hour=17, minute=30, second=0, microsecond=0)
	today6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
	if now>today4pm and now<today45pm:
		slot="4"
	elif now>today45pm and now<today5pm:
		slot="4.5"
	elif now>today5pm and now<today55pm:
		slot="5"
	elif now>today55pm and now<today6pm:
		slot="5.5"
	print slot
	if a:
		utype=1
		
		profile=Appointment.objects.filter(Student_id=curr_user.id,Date=datetime.date.today(),Time=slot)
		if not profile:
			return HttpResponse("No appointment for you right now")
		
		
		                        
		sender,to= str(profile[0]).split(":")
	else:
		utype=2
		with connection.cursor() as cursor:
				cursor.execute('select id from IT_counsellor where counsellor_id=%d'%(curr_user.id))
				Counsellor_id=cursor.fetchone()
				
		profile=Appointment.objects.filter(Counsellor_id=Counsellor_id,Date=datetime.date.today(),Time=slot)
		
		if not profile:
			return HttpResponse("No appointment right now")

		to,sender= str(profile[0]).split(":")
		
		
		
		
					
	return render(request,'chat2.html',{'to':to,'sender':sender,'type':utype})
def register(request):
	context=RequestContext(request)
	registered=False
	if request.method=='POST':
		user_form=StudentForm(data=request.POST)
		profile_form=StudentProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.student=user
			profile.save()
			registered=True
		else:
			print user_form.errors,profile_form.errors
	else:
                user_form = StudentForm()
                profile_form = StudentProfileForm()

	return render(request,"signuppage.html",{'user_form': user_form,'profile_form': profile_form, 'registered': registered},context )


def user_login(request):
	next = request.GET.get('next', '/appointment/')
	context=RequestContext(request)
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Your account has been disabled")
		else:
			return HttpResponse("Invalid login details")
	else:
		return render(request,'loginpage.html',{'redirect_to': next},context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/home')

@login_required
def feedback(request):
	feedback=" "
	if request.method=='POST':
		feedback=request.POST['feedback']
		fback=Feedback(Student=auth(request)['user'],Date=datetime.date.today(),Time=datetime.datetime.now().time(),feedback=feedback)
		fback.save()
		return HttpResponseRedirect('/home')
	return render(request,'feedback.html',)

@login_required
def myprofile(request):
	stu=auth(request)['user']
	li=[]
	profile=[]
	li=Appointment.objects.filter(Student=stu,Date__gte=datetime.date.today()).order_by('Time').order_by('Date')
	print li

	utype=1
	profile=Student.objects.filter(student_id=stu.id)
	if not profile:
				profile=Counsellor.objects.filter(counsellor=stu)
				print profile
				
				li=Appointment.objects.filter(Counsellor_id=profile[0],Date__gte=datetime.date.today()).order_by('Time').order_by('Date')
				utype=0
	return render(request,'appointments.html',{'appointment':li,'profile':profile,'type':utype})
@login_required
def ragging(request):
	
	if request.method=='POST':
		From=request.POST['name']
		Complain=request.POST['complain']
		print Complain
		msg = MIMEText(Complain)
	
		msg['Subject'] = 'Ragging Complaint by %s'% From
		msg['From'] = 'iitbhu.counselling@gmail.com'
		msg['To'] = 'chaitanya.bhatia.cse15@itbhu.ac.in'
		try:
			s = smtplib.SMTP('smtp.gmail.com',587)
			s.ehlo()
			s.starttls()
			s.login('iitbhu.counselling@gmail.com','counsel@iitbhu')
			s.sendmail('iitbhu.counselling@gmail.com', 'chaitanya.bhatia.cse15@itbhu.ac.in', msg.as_string())
			s.quit()
			return HttpResponse("Your Complaint has been registered and action will be taken as soon as Possible")
		except:
			return HttpResponse("Network Error. Please try again later")
	return render(request,"rag.html",)
