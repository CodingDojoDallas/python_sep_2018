from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	return render(request,'index.html')

def results(request):
	if request.method == "POST":
		print(request.POST)
		print(request.POST['name'])
		return render(request, 'results.html')

def reset(request):
	return redirect('/survey')