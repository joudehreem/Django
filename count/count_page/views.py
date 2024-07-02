from django.shortcuts import render,redirect

# Create your views here.


# Ensure the user not in session, if in session increment +1
def counter(request):
  if 'count' not in request.session:
    request.session['count']=0
  else:
      request.session['count']+=1
  return render(request,'index.html')

#Increment +2
def add_two(request):
  
  request.session['count']+=2
  return redirect('/')


# clears a specific key or use clear to delete all session
def clear(request):
  #request.session.clear()	
  del request.session['count']
  return redirect('/')