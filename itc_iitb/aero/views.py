from django.shortcuts import render

def index(request):
    return render(request,'aero/homepages/homepages.html');

def vision(request):
    return render(request,'aero/visions/visions.html');

def events(request):
	return render(request,'aero/events/events.html');

def team(request):
	return render(request,'aero/teams/teams.html');

def rcplane(request):
	return render(request,'aero/rcplanes/rcplanes.html');

def gallery(request):
	return render(request,'aero/gallery/gallery.html');

def search(request):
	return render(request,'aero/search/search.html');
