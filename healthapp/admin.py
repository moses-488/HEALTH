from django.contrib import admin
from healthapp.models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Myappointment)






def __str__(self):
    return self.fullname 
    