from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    data = {
    1: {
        "name": "Nebulosa de Carina",
        "credits": "webbtelescope.org / NASA / James Webb"
    },
    2: {
        "name": "Galáxia NGC 1079",
        "credits": "nasa.org / NASA / Hubble"
    }
}
    
    return render(request, 'galery/index.html', {"cards": data})
def image(request):
    return render(request, 'galery/image.html')