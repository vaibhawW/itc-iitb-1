from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'krittika/home.html',{'title':'Home'})

def vision(request):
	return render(request,'krittika/vision.html',{'title':'Vision'})

# Lectures
def lectures(request):
	return render(request,'krittika/events/lectures.html',{'title':'Lectures'})

lectureCount=2
def lectureOne(request,blog_num):
	if int(blog_num)<=lectureCount:
		return render(request,'krittika/events/lectures/%s.html' % blog_num, {'title':'Lecture %s ' % blog_num})
	else :
		#return lectures(request);
		return lectures(request)

# Group Discussion

def GDs(request):
	return render(request,'krittika/events/GDs.html',{'title':'GD'})

gdCount=3
def gdOne(request,blog_num):
	if int(blog_num)<=gdCount:
		return render(request,'krittika/events/discussions/%s.html' % blog_num, {'title':'Discussion %s ' % blog_num})
	else :
		#return lectures(request);
		return GDs(request)

def trips(request):
	return render(request,'krittika/events/trips.html',{'title':'trips'})

tripCount=2
def tripOne(request,blog_num):
	if int(blog_num)<=gdCount:
		return render(request,'krittika/events/trips/%s.html' % blog_num,{'title':'Trip %s' % blog_num})
	else :
		return trips(request)

def photos(request):
	return render(request,'krittika/gallery/photos.html',{'title':'Photos'})

def VR(request):
	return render(request,'krittika/gallery/VR.html',{'title':'VR'})

def about(request):
	return render(request,'krittika/about.html',{'title':'About Krittika'})

def team(request):
	return render(request,'krittika/team.html',{'title':'Team'})

def resources(request):
	return render(request,'krittika/resources.html',{'title':'Resources for Basics of Astronomy'})

def books(request):
	return render(request,'krittika/resources/books.html',{'title':'Books'})

def telescope(request):
	return render(request,'krittika/resources/telescope.html',{'title':'Building-Telescope'})

def celistial(request):
	return render(request,'krittika/resources/celestial.html',{'title':'Celestial-Mechanics'})

def basics(request):
	return render(request,'krittika/resources/basics.html',{'title':'Basics'})



