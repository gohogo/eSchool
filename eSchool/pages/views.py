from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	return render(request,'index.html')
	
def home_test(request):
	return render(request,'hometest.html')