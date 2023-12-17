
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
 #   return HttpResponse("Hello World")
     return render(request, 'home.html', { 'name' : 'SomdattaSaha'})
 
def addition(request):
    
    num1 = int(request.POST['num1'])
      
    num2 = int(request.POST['num2'])
    
    sum1 = num1 + num2

    return render(request,'results.html', { 'res1' : sum1 })
 

