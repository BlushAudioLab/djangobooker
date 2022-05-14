from django.contrib import admin
from .models import Type, Event, Room


class EventAdmin(admin.ModelAdmin):
    list_display = ('title','room','owner','timebooked')
admin.site.register(Event, EventAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','type','capacity','description')
admin.site.register(Room, RoomAdmin)


admin.site.register(Type)
