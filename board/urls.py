
from django.urls import path

from board import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('room/<int:id>/edit/',views.editRoom, name="edit-room"),
    path('room/<int:id>/',views.publicRoom, name="public-room")
]

