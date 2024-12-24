from django.contrib import admin
from .models import *

# admin.site.register(Property)
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'address', 'city', 'price', 'property_type')

  
    list_filter = ('city', 'property_type')  

   
    search_fields = ('name', 'address', 'city')

admin.site.register(Property, PropertyAdmin)
