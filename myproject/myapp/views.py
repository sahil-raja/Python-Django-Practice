from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'name': 'John',
        'age': 20,
        'nationality': 'Nigerian'
    }
    return render(request, 'index.html', context)


def counter(request):
    text = request.POST['text']
    total_count_words = len(text.split(' '))
    return render(request, 'counter.html', {'count': total_count_words})
