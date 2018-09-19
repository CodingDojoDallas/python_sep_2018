from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random
def index(request):
    if 'yourgold' not in request.session:
        request.session['yourgold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    context = {
        'farm' : random.randrange(10,21),
        'cave' : random.randrange(5,11),
        'house' : random.randrange(2,6),
        'casino' : random.randrange(-50,51)
    }
    return render(request, 'gold_app/index.html', context= context)

def Process(request):
    if request.method == 'POST':
        if request.POST['place'] == 'farm':
            request.session['yourgold'] += int(request.POST['farm'])
            earned = request.POST['farm']
        if request.POST['place'] == 'cave':
            request.session['yourgold'] += int(request.POST['cave'])
            earned = request.POST['cave']
        if request.POST['place'] == 'house':
            request.session['yourgold'] += int(request.POST['house'])
            earned = request.POST['house']
        if request.POST['place'] == 'casino':
            request.session['yourgold'] += int(request.POST['casino'])
            earned = request.POST['casino']
        tempact = request.session['activity']
        tempact.reverse()
        if int(earned) > 0:
            tempact.append({'text': f"Earned {earned} gold from the {request.POST['place']}! at ({datetime.now()})", 'color': 'green'})
        if int(earned) <= 0:
            tempact.append({'text': f"Entered a casino and lost {earned} gold... Ouch! at ({datetime.now()})", 'color': "red"})
        tempact.reverse()
        request.session['activity'] = tempact
        return redirect('/')