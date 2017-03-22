from django.conf.urls import url
from . import views


urlpatterns= [
	url(r'^home/$',views.home,name='home'),
	url(r'^appointment/$',views.appointment,name='appointment'),
	url(r'^login/',views.user_login,name='login'),
	url(r'^info/$',views.importantinfo,name='importantinfo'),
	url(r'^feedback/$',views.feedback,name='feedback'),
	url(r'^register/$', views.register,name='register'),
	url(r'^logout/$',views.user_logout,name='logout'),
	url(r'^newstudents/$',views.newstudents,name='newstudents'),
	url(r'^map/$',views.map,name='map'),
	url(r'^profile/$',views.myprofile,name='myprofile'),
	url(r'^ragging/$',views.ragging,name="ragging"),
	url(r'^chat/$',views.chat,name="chat"),
	url(r'^emotional/$',views.emotional,name="emotional"),
	url(r'^academic/$',views.academic,name="academic"),
]
