import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    print(room_name)
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'room_name': room_name
    }
    print(context['room_name_json'])
    return render(request, "chat/room.html", context)


