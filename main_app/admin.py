from django.contrib import admin

# Register your models here.
from .models import Artist, Song, Playlist # import the models from models.py

admin.site.register(Artist) # this line will add the model to the admin panel
admin.site.register(Song) 
admin.site.register(Playlist)