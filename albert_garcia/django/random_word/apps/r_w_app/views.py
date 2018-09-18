from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):
    request.session['random'] = get_random_string(14)
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1

    return render(request, "r_w_app/index.html")

def generate(request):
    if request.method == 'POST':
        return redirect('/') 

def reset(request):
    del request.session['attempt']
    return redirect('/')