from django.db import models

import uuid

def get_token():
    return uuid.uuid4().hex

class Room(models.Model):
    name = models.CharField(max_length=64)
    token = models.CharField(max_length=32, default= get_token)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self) -> str:
        return self.name

class Participant(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    name = models.CharField(max_length=64,blank=False)
    score = models.IntegerField(default=0)

    class Meta:
        unique_together = ['room','name']
    

    def __str__(self) -> str:
        return "{} - {}".format(self.room.name,self.name)