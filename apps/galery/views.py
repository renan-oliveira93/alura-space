from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galery.models import Picture
from apps.galery.forms import PictureForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('sign_in')
    pictures = Picture.objects.order_by("-picture_date").filter(published=True)
    return render(request, 'galery/index.html', {"cards": pictures})

def news(request):
    return render(request, 'news/index.html')

def image(request, clicked_picture_id):
    clicked_picture = get_object_or_404(Picture, pk=clicked_picture_id)
    return render(request, 'galery/image.html', {"picture": clicked_picture})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('sign_in')
    pictures = Picture.objects.order_by("-picture_date").filter(published=True)
    if 'search' in request.GET:
        search_input_value = request.GET['search']
        if search_input_value:
            pictures = pictures.filter(name__icontains=search_input_value)
    return render(request, "galery/index.html", {"cards": pictures})

def add_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('sign_in')
    form = PictureForms
    if request.method == 'POST':
        form= PictureForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagem cadastrada com sucesso")
            return redirect('index')
    return render(request, 'galery/add_view.html', {'form': form})

def edit_view(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    form = PictureForms(instance=picture)

    if request.method == 'POST':
        form = PictureForms(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagem atualizada com sucesso")
            return redirect('index')
    return render(request, 'galery/edit_view.html', {'form': form, 'picture_id': picture_id}) 

def delete_view(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    picture.delete()
    messages.success(request, 'Imagem deletada com sucesso')
    return redirect('index')

def filter(request, category):
    pictures = Picture.objects.order_by("-picture_date").filter(published=True, category=category)
    return render(request, 'galery/index.html', {'cards': pictures} )