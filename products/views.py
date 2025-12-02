from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Friends! Greetings from Django | Now on a server! | DEV Yoni | Python!")

def new(request):
    return HttpResponse("New Products added | DEV Yoni | Python!")
