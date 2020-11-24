from django.urls import path
from . import views # 1

urlpatterns = [
    path('template1', views.template_1),
    path('template2', views.template_2),
    path('template3', views.template_3),
]