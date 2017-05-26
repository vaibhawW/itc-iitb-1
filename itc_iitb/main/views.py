from django.shortcuts import render

# Create your views here.
def index(request):
    arr={'title':'STAB|IITB'}
    return render(request,'main/index.html',arr)

def alumni(request):
    return render(request,'alumni/alumni.html')

def team2012(request):
    return render(request,'team/2012-13/team.html')

def team2013(request):
    return render(request,'team/2013-14/team.html')

def team2014(request):
    return render(request,'team/2014-15/team.html')

def team2015(request):
    return render(request,'team/2015-16/team.html')

def team2016(request):
    return render(request,'team/2016-17/team.html')

def team2017(request):
    return render(request,'team/2017-18/team.html')

def gcrankings(request):
    return render(request,'TechGC/Rankings/2016-17.html')

def hof(request):
    return render(request,'HallofFame/hof.html')

def login(request):
    return render(request,'main/login.html')
