from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'biotech/index.html')

def events(request):
	return render(request,'biotech/events.html')

def blog(request):
	return render(request,'biotech/blog.html')

def tutorials(request):
	return render(request,'biotech/tutorials.html')

def contact(request):
	return render(request,'biotech/contact.html')

blogCount=1
def blogNum(request,blog_num):
	if int(blog_num)<=blogCount:
		return render(request,'biotech/blogs/%s.html' % blog_num)
	else :
		return blog(request);

tutCount=1
def tutNum(request,tut_num):
	if int(tut_num)<=tutCount:
		return render(request,'biotech/tutorials/%s.html' % tut_num)
	else :
		return tutorials(request);