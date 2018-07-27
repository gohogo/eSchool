from django.http import HttpResponse
from django.shortcuts import render
# shop/product/list.html
def home_page(request):
	return render(request,'pages/homepage.html',
				{'section': 'homepage'})

def about_page(request):
	return render(request,'pages/aboutpage.html',
				{'section': 'aboutpage'})	

def service_page(request):
	return render(request,'pages/servicepage.html',
				{'section': 'servicepage'})	

def project_page(request):
	return render(request,'pages/projectpage.html',
				{'section': 'projectpage'})

def course_page(request):
	return render(request,'pages/coursepage.html',
				{'section': 'coursepage'})

def contact_page(request):
	return render(request,'pages/contactpage.html',
				{'section': 'contactpage'})

def location_page(request):
	return render(request,'pages/baidumap.html')

def home_test(request):
	return render(request,'pages/hometest.html')