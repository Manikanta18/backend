from django.contrib import admin
from .models import Contact, Event, Alumni

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note')

class EventAdmin(admin.ModelAdmin):
    list_display = ('testname', 'date', 'description')

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'company', 'country')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Alumni, AlumniAdmin)

