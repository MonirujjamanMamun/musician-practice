from django.shortcuts import render, redirect
from .forms import AddMusiciansForms
from .models import Musician
# Create your views here.


def add_musicians(request):
    if request.method == 'POST':
        musician_form = AddMusiciansForms(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musicians')
    else:
        musician_form = AddMusiciansForms()
    return render(request, 'add_musicians.html', {'form': musician_form})


def edit_musicians(request, id):
    editable_data = Musician.objects.get(pk=id)
    musician_form = AddMusiciansForms(instance=editable_data)
    if request.method == 'POST':
        musician_form = AddMusiciansForms(request.POST, instance=editable_data)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request, 'add_musicians.html', {'form': musician_form})
