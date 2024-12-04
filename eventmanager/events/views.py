from django.shortcuts import render
from.models import Event


def event_list(request):
 event_list = Event.objects.all()
 return render(request,'events/even_list.html', {'event_list':event_list})

def add_event(request):
    return render (request,'events/add_event.html')


def edit_event(request):
    return render (request,'events/edit_event.html')