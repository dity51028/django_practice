""" Controller of our whole structure """
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin

def home(request):
   return render(request, 'index.html')
def about(request):
    return HttpResponse("About Us")
def contact(request):
    return HttpResponse("Contact Us")
def services(request):
    return HttpResponse("Services")