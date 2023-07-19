from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse("<marquee><i>This is my first string..</i></marquee>")