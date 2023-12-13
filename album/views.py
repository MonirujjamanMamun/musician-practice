from django.shortcuts import render, redirect
from .forms import AddAlbumForms
from .models import Album
# Create your views here.


def add_album(request):
    if request.method == 'POST':
        album_form = AddAlbumForms(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = AddAlbumForms()
    return render(request, 'add_album.html', {"form": album_form})


def album_edit(request, id):
    album_data = Album.objects.get(pk=id)
    album_form = AddAlbumForms(instance=album_data)
    if request.method == 'POST':
        album_form = AddAlbumForms(request.POST, instance=album_data)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')

    return render(request, 'add_album.html', {"form": album_form})


def album_delete(request, id):
    album_data = Album.objects.get(pk=id)
    album_data.delete()
    return redirect('homepage')
