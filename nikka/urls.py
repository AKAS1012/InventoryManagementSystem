from .views import login, logout_page
from django.urls import path

urlpatterns = [

    path('login/', login, name='login'),
    path('logout/', logout_page, name='logout')
]
