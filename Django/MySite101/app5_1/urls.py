from django.urls import path
from . import views # 1

urlpatterns = [
    path('variables', views.display_variables),
    path('filters', views.display_filters),
    path('tags', views.display_tags),
]