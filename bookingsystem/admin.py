from django.contrib import admin
from .models import Type, Event, Room

admin.site.register(Event)
admin.site.register(Type)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','type','capacity','description')
admin.site.register(Room, RoomAdmin)


