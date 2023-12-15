from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Room, Message

# Create your views here.


def login(request):
    return render(request, 'login.html')


def process_login(request):
    username = request.POST.get('username')
    room = request.POST.get('roomname')

    if Room.objects.filter(RoomId=room).exists():
        return redirect('rooms/' + room + '?username=' + username)
    else:
        new_room = Room.objects.create(RoomId=room)
        new_room.save()
        return redirect('rooms/' + room + '?username=' + username)


def room(request, RoomId):
    username = request.GET.get('username')
    room_details = Room.objects.get(RoomId=RoomId)
    return render(request, 'rooms2.html', {
        'username': username,
        'room': RoomId,
        'room_details': room_details
    })


def send_message(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message,
                                         user=username,
                                         room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def get_messages(request, RoomId):
    room_details = Room.objects.get(RoomId=RoomId)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
