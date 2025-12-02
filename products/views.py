from django.http import HttpResponse
from django.shortcuts import render


#URL = Uniform Resource Locator (meaning, address)
#producs -> index //Map /products with index
def index(request):
    return HttpResponse("Hello Friends! Greetings from Django | Now on a server! Very Cool!! | DEV Yoni | Python!")


def new(request):
    return HttpResponse("New Products added | DEV Yoni | Python!")
