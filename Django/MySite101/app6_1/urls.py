from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name="new"),
    path('insert/', views.insert),
    path('edit', views.edit, name="edit"),
    path('update/', views.update),
    path('display_delete', views.display_delete, name="display_delete"),
    path('delete/', views.delete),
]