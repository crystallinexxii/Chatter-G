from django.shortcuts import render, redirect
from chat.models import Room

# Create your views here.

def login(request):
    return render(request, 'login.html')


def process_login(request):
    username = request.POST.get('username')
    room = request.POST.get('roomname')
    if room == '' or username == '':
        return redirect('login')

    if Room.objects.filter(RoomId=room).exists():
        return redirect('rooms/' + room + '?username=' + username)
    else:
        new_room = Room.objects.create(RoomId=room)
        new_room.save()
        return redirect('rooms/' + room + '?username=' + username)

