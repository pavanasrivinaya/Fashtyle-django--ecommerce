from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    name = "pavana"
    age = 23
    context = {
        'name':name,
        'age':age
    }
    return render(request, 'index.html', context)