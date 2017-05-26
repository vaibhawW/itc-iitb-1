from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'mnp/index.html')

def about(request):
	return render(request,'mnp/about.html')

def blog(request):
	return render(request,'mnp/blog/default/index.html')

blogCount = 7
def blogNo(request,blog_num):
	if int(blog_num)<=blogCount and int(blog_num)>0:
		return render(request,'mnp/blog/%s/index.html' %blog_num)
	else :
		return blog(request)

def projects(request):
	return render(request,'mnp/projects/index.html');

def events(request):
	return render(request,'mnp/events/index.html');

