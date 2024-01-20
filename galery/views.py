from django.shortcuts import render, get_object_or_404
from galery.models import Picture

def index(request):
    pictures = Picture.objects.all()
    return render(request, 'galery/index.html', {"cards": pictures})
def image(request, clicked_picture_id):
    clicked_picture = get_object_or_404(Picture, pk=clicked_picture_id)
    return render(request, 'galery/image.html', {"picture": clicked_picture})