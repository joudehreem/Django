
# Create your views here.
from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime
    
def index(request):
    now = datetime.now()
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "now": now.strftime("%Y-%m-%d %H:%M %p"),
    }
    
    return render(request,'index.html', context)


