from django.http import HttpResponse
from django.shortcuts import render
from .models import Books



def index(request):
    return render(request, 'Books/index.html')
def dtail(request, title):
    return HttpResponse("You're looking at question %s." % title)