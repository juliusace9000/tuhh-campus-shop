from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome! This is the Website of the TUHH's campus shop...")

# Create your views here.
