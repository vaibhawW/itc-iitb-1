from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'srg/home/index.html')

def about(request):
    return render(request,'srg/about/about.html')

def events(request):
    return render(request,'srg/events/events.html')

def team(request):
    return render(request,'srg/team/team.html')

def teamstruct(request):
    return render(request,'srg/teamstruct/teamstruct.html')
