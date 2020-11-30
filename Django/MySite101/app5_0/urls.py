from django.urls import path
from . import views # 1

urlpatterns = [
    path('filters/', views.filters),
    path('tags/', views.tags),
]