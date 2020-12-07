from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index),
    path('display_new_form', views.display_new_form),
    path('save_new_person/', views.save_new_person),
]