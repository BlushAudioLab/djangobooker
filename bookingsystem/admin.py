from django.contrib import admin
from .models import Item, ItemType, ItemArea, RoomType, Event, Room


class EventAdmin(admin.ModelAdmin):
    list_display = ('title','room','owner','timebooked')
admin.site.register(Event, EventAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','type','capacity','description')
admin.site.register(Room, RoomAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','barcode','description','type', 'area')
admin.site.register(Item, ItemAdmin)

admin.site.register(RoomType)
admin.site.register(ItemType)
admin.site.register(ItemArea)
