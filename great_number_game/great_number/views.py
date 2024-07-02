from django.shortcuts import render, redirect
import random
def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    if 'answer' not in request.session:
        request.session['answer'] = 0
    if 'color' not in request.session:
        request.session['color'] = 0
    if 'attempt' not in request.session:
        request.session['attempt'] = 0

    return render(request, 'index.html')

def random_number(request):
    if request.method == 'POST':
        guess = int(request.POST['random'])
        request.session['attempt'] += 1

        if guess < request.session['number']:
            request.session['answer'] = 'too low!'
            request.session['color'] = 'red'
        elif guess > request.session['number']:
            request.session['answer'] = 'too high!'
            request.session['color'] = 'blue'
        else:
            request.session['answer'] = 'correct'
            request.session['color'] = 'green'

    return redirect('/')

def again(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/')