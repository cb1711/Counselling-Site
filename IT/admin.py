from django.contrib import admin

from .models import Student,Counsellor,Appointment,Feedback,Message

from .models import News
admin.site.register(Student)
admin.site.register(News)
admin.site.register(Counsellor)
admin.site.register(Appointment)
admin.site.register(Feedback)
#admin.site.register(Message)
