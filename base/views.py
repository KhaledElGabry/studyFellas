from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': "Let's Learn python!"},
    {'id': 2, 'name': "Let's Learn Node.js!"},
    {'id': 3, 'name': "Back-End Developers"},
    {'id': 4, 'name': "Practice with me :)"},
    {'id': 5, 'name': "Let's Engage with DevOps !!"},
]

def home(request):
    context={'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'room.html')
