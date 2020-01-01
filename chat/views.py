from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

def vs(request):
    return render(request, 'chat/vs.html', {
        'room_name_json': mark_safe(json.dumps("vs"))
    })

def parents(request):
    return render(request, 'chat/parents.html', {
        'room_name_json': mark_safe(json.dumps("vs"))
    })
