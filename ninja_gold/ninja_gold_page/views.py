from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'POST':
        building = request.POST['building']
        gold_earned = earn_gold()[building]
        update_gold(request, building, gold_earned)
    return redirect('/')

def reset_gold(request):
    request.session.flush()
    return redirect('/')

def update_gold(request, building, gold_earned):
    request.session['gold'] += gold_earned
    activity = create_activity(building, gold_earned)
    activities = request.session.get('activities', [])
    activities.append(activity)
    request.session['activities'] = activities

def create_activity(building, gold_earned):
    activity = {
        'building': building,
        'gold': gold_earned,
        'time': datetime.now().strftime("%B %dth %Y %H:%M %p"),
        'color': 'earn' if gold_earned >= 0 else 'lost'
    }
    return activity

def earn_gold():
    buildings = {
        'farm': random.randint(10, 20),
        'cave': random.randint(10, 20),
        'house': random.randint(10, 20),
        'Quest': random.randint(-50, 50)
    }
    return buildings

