from django.urls import path
from apps.galery.views import \
    index, image, search, add_view, edit_view, delete_view, filter, news

urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('image/<int:clicked_picture_id>', image, name='image'),
    path('search', search, name="search"),
    path('add-view', add_view, name='add_view'),
    path('edit-view/<int:picture_id>', edit_view, name='edit_view'),
    path('delete-view/<int:picture_id>', delete_view, name='delete_view'),
    path('filter/<str:category>', filter, name='filter'),
]