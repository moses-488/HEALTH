from django.contrib import admin
from healthapp.models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Myappointment)
admin.site.register(Transaction)







def __str__(self):
    return self.fullname 
    