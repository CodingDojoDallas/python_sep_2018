from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "placeholder to later display all list of blogs"
	return HttpResponse(response)
def new(request):
	response = "Placeholder to display a new form to create a blog"
	return HttpResponse(response)
def create(request):
	return redirect('/')
def number(request,number):
	response = "Placeholder to hold "+number
	return HttpResponse(response)
def edit(request,number):
	response = "Placeholder to edit "+number
	return HttpResponse(response)
def destroy(request,number):
	return redirect('/')