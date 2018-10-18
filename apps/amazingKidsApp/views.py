from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from django.views.generic import TemplateView

def index (request):
    print "CHECKPOINT: Thanks for joining us. You are going to Landing."
    return render(request, 'amazingKidsApp/index.html')

def process(request):
    print "CHECKPOINT: Thanks for joining us. You are processing to corriculum."
    return redirect('amazingKidsApp/curriculum')

def corriculum(request):
    print "CHECKPOINT: Thanks for joining us. You are going to corriculum."
    return render(request, "amazingKidsApp/corriculum.html")