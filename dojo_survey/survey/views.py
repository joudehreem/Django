from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
        name = request.POST['name']
        location = request.POST['location']
        language = request.POST['favlang']
        comment = request.POST['comment']
        context = {
            "name": name,
            "location": location,
            "language": language,
            "comment": comment,
        }
        print(name)
        print(location)
        print(language)
        print(comment)
        return render(request,'result.html', context)


