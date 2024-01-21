from django.shortcuts import render, get_object_or_404
from galery.models import Picture

def index(request):
    pictures = Picture.objects.order_by("-picture_date").filter(published=True)
    return render(request, 'galery/index.html', {"cards": pictures})
def image(request, clicked_picture_id):
    clicked_picture = get_object_or_404(Picture, pk=clicked_picture_id)
    return render(request, 'galery/image.html', {"picture": clicked_picture})

def search(request):
    pictures = Picture.objects.order_by("-picture_date").filter(published=True)
    if 'search' in request.GET:
        search_input_value = request.GET['search']
        if search_input_value:
            pictures = pictures.filter(name__icontains=search_input_value)
    return render(request, "galery/search.html", {"cards": pictures})