from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from board.forms import RoomForm
from board.models import Room, Participant

def home(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            messages.success(request,"Room {} created successfully!".format(room.name))
            request.session['onamboard_token'] = room.token
            return redirect('edit-room',id=room.id)

    form = RoomForm()
    return render(request,'board/home.html',{'form':form})


def editRoom(request,id):
    room = Room.objects.filter(id=id).first()
    if room:
        if request.session.get('onamboard_token','') == room.token:
            if request.method == "POST":
                if "add" in request.POST and request.POST['name'] != '':
                    try:
                        add_participant  = Participant(room=room,name=request.POST['name'])
                        add_participant.save()
                        messages.success(request,"Person added successfully!")
                    except:
                        messages.error(request,"Error: Adding person")
                elif "remove" in request.POST:
                    try:
                        remove_participant = Participant.objects.get(id=request.POST['participant_id'])
                        remove_participant.delete()
                        messages.success(request,"Person removed successfully!")
                    except:
                        messages.error(request,"Error: Removing person")
            
                elif "update" in request.POST:
                    try:
                        edit_participant = Participant.objects.get(id=request.POST['participant_id'])
                        edit_participant.name = request.POST['name']
                        edit_participant.score = request.POST['score']

                        edit_participant.save()
                        messages.success(request,"Updation successful!")
                    except:
                        messages.error(request,"Error: Updating person")
            participants = Participant.objects.filter(room=room).order_by('-score')      
            return render(
                request,'board/edit_room.html',
                {
                    'room_name':room.name,
                    'participants':participants
                }
            )
        messages.warning(request,"Unauthorized: No Edit Premission, Only View Premission")
        return redirect('public-room',id=id)
    
    else:
        messages.error(request,"Error: Room not found")
        return redirect('home')


def publicRoom(request,id):
    room = Room.objects.filter(id=id).first()
    if room:
        participants = Participant.objects.filter(room=room).order_by('-score')    
        return render(
            request,'board/public_room.html',
            {
                'room_name':room.name,
                'participants':participants
            }
        )
    else:
        messages.error(request,"Error: Room not found")
        return redirect('home')


def page_not_found(request,exception):
    return render(request,"error/404.html")


def internal_error(request):
    return render(request,"error/500.html")