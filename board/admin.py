from django.contrib import admin

from board.models import Room, Participant

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','token','created_at']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['room_name','name','score']

    def room_name(self,obj):
        return obj.room.name