from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {}
    return render(request, template_name="chat/index.html", context=context)

@login_required
def room(request, room_name):
    context = {'room_name': room_name}
    return render(request=request, template_name='chat/room.html', context=context)
