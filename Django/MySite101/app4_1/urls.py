from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index),
    path('static_contents', views.static_contents),
]