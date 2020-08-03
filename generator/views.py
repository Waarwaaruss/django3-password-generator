from django.shortcuts import render
from django. http import HttpResponse
import random
# Create your views here.

def about(request):
    return render(request, 'generator/about.html')
    
def home(request):
    return render(request, 'generator/home.html')
def password(request):

    characters = list('abcdefghijklmopqrstuvwxyz')
    charactersUp = list('ABCDEFGHIKLMNOPQRSTVXYZ')

    if request.GET.get('uppercase'):
        characters.extend(charactersUp)
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*/\|'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})

