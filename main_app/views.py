from django.shortcuts import render
from django.views import View # handles requests
from django.http import HttpResponse # handles sending a type of response
from django.views.generic.base import TemplateView

# Create your views here.

#here we will be creating a class called Home and extending it from the View class 
class Home(View):

    # Here we are adding a method that will be ran when we are dealing with a GET request
    def get(self, request):
        #here we are returning a generic response
        #this is similar to response.send() in express
        return HttpResponse("Spotify Home")

class About(View):

    def get(self, request):
        return HttpResponse("Spotify About")

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"
