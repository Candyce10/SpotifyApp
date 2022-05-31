from django.contrib import admin

# Register your models here.
from .models import Artist # import the Artist model from models.py

admin.site.register(Artist) # this line will add the model to the admin panel