from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def team(request):
    return render(request,'team/2017-18/team.html')

def gcrankings(request):
    return render(request,'TechGC/Rankings/2016-17.html')

def login(request):
    return render(request,'main/login.html')
