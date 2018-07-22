from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	return render(request,'homepage.html')

def about_page(request):
	return render(request,'aboutpage.html')	

def service_page(request):
	return render(request,'servicepage.html')	

def project_page(request):
	return render(request,'projectpage.html')

def course_page(request):
	return render(request,'coursepage.html')

def contact_page(request):
	return render(request,'contactpage.html')

def location_page(request):
	return render(request,'baidumap.html')

def home_test(request):
	return render(request,'hometest.html')