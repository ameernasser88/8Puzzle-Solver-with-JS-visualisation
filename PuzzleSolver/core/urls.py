from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('solve/', solve , name='solve'),
]
