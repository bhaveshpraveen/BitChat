import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from django.utils.safestring import mark_safe

from .models import Room

@login_required
def index(request):
    return render(request, 'chat/index.html', {})

# TODO: Render previous messages to template
@login_required
def room(request, room_name):
    obj, created = Room.objects.get_or_create(slug=slugify(room_name))
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'room_name': room_name
    }
    if not created:
        context['messages'] = obj.messages.all().order_by('created')[0:50]

    return render(request, "chat/room.html", context)


class RoomList(ListView):
    model = Room
    template_name = ''



