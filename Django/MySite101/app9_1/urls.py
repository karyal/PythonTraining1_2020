from django.urls import path
from . import views # 1

urlpatterns = [
    path('display_form_1', views.display_form_1),
    path('get_form_1/', views.get_form_1),
]