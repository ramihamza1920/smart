from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(myProject)

#class myProjectAdmin(admin.ModelAdmin):
 #   list_display = ['polygon_id', 'geomp']