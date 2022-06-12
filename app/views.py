from django.shortcuts import render
from django.http  import HttpResponse


app_name= 'app'

def home(request):
    return HttpResponse('Welcome to the world of Awards - Vote your project!')
