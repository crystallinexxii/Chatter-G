from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import datetime
from pprint import pprint

from .models import Room, Message

# Create your views here.


def room(request, RoomId):
    username = request.GET.get('username')
    room_details = Room.objects.get(RoomId=RoomId)
    return render(request, 'room.html', {
        'username': username,
        'room': RoomId,
        'room_details': room_details
    })


def send_message(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    print(message, username, room_id)

    if message.strip() != '':
        new_message = Message.objects.create(value=message.strip(),
                                             user=username,
                                             room=Room.objects.get(id=room_id))
        new_message.save()
        return HttpResponse('Message sent successfully')
    else:
        return HttpResponse('Message cannot be empty')


def get_messages(request, RoomId):
    room_details = Room.objects.get(RoomId=RoomId)

    messages = Message.objects.filter(room=room_details.id)

    m = messages.values()
    for i in m:
        i['date'] = (i['date'] + datetime.timedelta(hours=5, minutes=30)).strftime('%I:%M %p')

    return JsonResponse({"messages": list(m)})