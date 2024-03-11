from django.contrib import admin
from .models import Room, Message
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Room, RoomAdmin)
admin.site.register(Message)