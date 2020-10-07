from django.contrib import admin
from .models import Inspections, User, Facility, Type, AWPForm

# Register your models here.

admin.site.register(Inspections)
admin.site.register(User)
admin.site.register(Facility)
admin.site.register(Type)
admin.site.register(AWPForm)