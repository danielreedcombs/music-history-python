
from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Song


# Create your views here.
def index(request):
    artist_list = Artist.objects.all()
    artists = {'artist_list': artist_list}
    return render(request, 'history/index.html', artists)

def views(request, artist_name):
    return HttpResponse(f"You're looking at the results of {artist_name}.")

def detail(request, artist_id):
    song_list = Song.objects.filter(artist_id_id = artist_id)
    print(song_list)
    context = {'song_list' : song_list}
    return render(request, 'history/detail.html', context)


