from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime
  # the index function is called when root is visited
def index(request):
	if 'words' not in request.session:
		request.session['words'] = []
	if 'time' not in request.session:
		request.session['time']= str(datetime.now())
	return render(request,'session_words/index.html')

def input(request):
	if request.method =="POST":
		request.session['time'] = str(datetime.now())
		print("This is request.POST*****",request.POST)
		print("I've visited INPUT")
		temp_list = request.session['words']
		word = request.POST
		temp_list.append(word)
		request.session['words'] = temp_list
		print("This is word parameters******",word)
		print("SESSION IS NOW:",request.session['words'])

		return redirect('/sessions')