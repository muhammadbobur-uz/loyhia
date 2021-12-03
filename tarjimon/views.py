from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat

def index(requests):
    s = requests.GET.get('q', '')
    n = Lugat.objects.filter(ingilizcha__contains = s).all()

    return render(requests, 'index.html', {'n':n})

def salom(requests):
    return HttpResponse('<code>Assalomu alaykum !</code>')

