from django.urls import path
from apps.users.views import sign_in, sign_up, logout

urlpatterns = [
    path('sign_in', sign_in, name='sign_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('logout', logout , name='logout')
]
