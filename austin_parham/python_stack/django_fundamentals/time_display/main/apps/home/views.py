from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def home(request):
	response = "Test"
	print("Still in home")
	return HttpResponse(response)

def time(request):
	context = {
		"day": strftime("%b %d, %Y", gmtime()),
		"time": strftime("%I:%M %p", gmtime())
	}
	return render(request,'index.html', context)

