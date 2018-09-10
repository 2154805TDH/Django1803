from django.shortcuts import render
from django.http import HttpResponse
from .models import animal
# Create your views here.
def hello(request):
    return HttpResponse("hello")

def get_animal(request):
    name = animal.objects.all()
    return render(request, 'animal.html', context={'data':name})