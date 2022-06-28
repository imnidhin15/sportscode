# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Sportsform

from .models import event


def index(request):
    obj=event.objects.all()
    context= {
        'event_list':obj

    }
    return render(request,"index.html",context)
def detail(request,event_id):
    eve=event.objects.get(id=event_id)
    return render(request,"detail.html",{'event':eve})
def add_event(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        description = request.POST.get('description',)
        team = request.POST.get('team',)
        image = request.FILES['image']
        events = event(name=name,description=description,team=team,image=image,)
        events.save()
    return render(request,'add.html')
def update(request,id):
    sports = event.objects.get(id=id)
    form = Sportsform(request.POST or None, request.FILES, instance= sports)
    if form. is_valid():
        form.save()
        return redirect ('/')
    return render(request, 'edit.html',{'form':form, 'sports':sports})
def delete(request,id):
    if request.method == 'POST':
        eevent = event.objects.get(id=id)
        eevent.delete()
        return redirect('/')
    return render(request,'delete.html')