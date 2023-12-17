from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):
 #   return HttpResponse("Hello World")
     dest1 = Destination()
     dest1.name = 'Mumbai'
     dest1.desc = 'Where the City Never Sleeps'
     dest1.img  = 'destination_1.jpg'
     dest1.price = 1000
     dest1.offer = False
     
     
     dest2 = Destination()
     dest2.name = 'Mumbai'
     dest2.desc = 'Where the City Never Sleeps'
     dest2.img  = 'destination_2.jpg'
     dest2.price = 700
     dest2.offer = True
     
     dest3 = Destination()
     dest3.name = 'Mumbai'
     dest3.desc = 'Where the City Never Sleeps'
     dest3.img  = 'destination_3.jpg'
     dest3.price = 600
     
     dests = [ dest1, dest2, dest3]
     
     
 #    return render(request, 'index.html', {'price' : 700})
 
     return render(request, 'index.html', {'dests' : dests })
