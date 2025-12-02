<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render


#URL = Uniform Resource Locator (meaning, address)
#producs -> index //Map /products with index
def index(request):
    return HttpResponse("Hello Friends! Greetings from Django | Now on a server! Very Cool!! | DEV Yoni | Python!")


def new(request):
    return HttpResponse("New Products added | DEV Yoni | Python!")
=======
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Friends! Greetings from Django | Now on a server! | DEV Yoni | Python!")

def new(request):
    return HttpResponse("New Products added | DEV Yoni | Python!")
>>>>>>> 28523f3dfcc043cc39b382f9a5758251ff77d63c
