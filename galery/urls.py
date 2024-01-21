from django.urls import path
from galery.views import index, image, search

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:clicked_picture_id>', image, name='image'),
    path('search', search, name="search"),
]