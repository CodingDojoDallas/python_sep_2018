from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def random(request):
	context = {
			'number': get_random_string(length=14)
		}
	if 'count' not in request.session:
		request.session['count'] = 1
		print("Count has been reset to 1!***")
	return render(request, 'random_word/index.html', context)

def generate(request):
	if request.method == "POST":
		print("Went to generate!")
		request.session['count'] += 1
		print(request.session['count'])
		return redirect('/random')

def reset(request):
	if request.method == "POST":
		del request.session['count']
		print("Count has been cleared!***")
		return redirect('/random')

# Create your views here.
