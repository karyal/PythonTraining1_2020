from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index),# call the index function of views.py file. # blank url # 2
]
