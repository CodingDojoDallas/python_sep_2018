from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    if 'words' not in request.session:
        request.session['words'] = [{"word": "Word", "added": '- added at', 'dt': "Datetime", "color": "Color", 'big': "Big"}]
        print(request.session['words'])
    return render(request, "words_app/index.html")

def Process(request):
    if request.method == 'POST':
        templist = request.session['words']
        templist.append({"word": request.POST['word'], "added": '- added at', 'dt': str(datetime.now()), "color": request.POST['color'], 'big': request.POST['big']})
        request.session['words'] = templist
        print(request.session['words'])
    return redirect('/')

def Clear(request):
    request.session.clear()
    return redirect('/')
