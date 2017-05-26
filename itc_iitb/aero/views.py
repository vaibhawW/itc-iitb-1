from django.shortcuts import render

def index(request):
    return render(request,'aero/homepages/homepages.html',{'title':'Aeromodelling Club'});

def vision(request):
    return render(request,'aero/visions/visions.html',{'title':'Vision - Aeromodelling Club'});

def events(request):
	return render(request,'aero/events/events.html',{'title':'Events - Aeromodelling Club'});

def team(request):
	return render(request,'aero/teams/teams.html',{'title':'Team - Aeromodelling Club'});

def rcplane(request):
	return render(request,'aero/rcplanes/rcplanes.html',{'title':'RC Planes - Aeromodelling Club'});

def gallery(request):
	return render(request,'aero/gallery/gallery.html',{'title':'Gallery - Aeromodelling Club'});

