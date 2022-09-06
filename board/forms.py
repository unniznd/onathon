from django import forms

from board.models import Room, Participant

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name',]

