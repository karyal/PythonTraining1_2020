from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index),
    path('display_new_form', views.display_new_form),
    path('save_new_person/', views.save_new_person),
    path('display_edit_form', views.display_edit_form),
    path('update_person/', views.update_person),
    path('delete_person/', views.delete_person),
    path('crud_model/', views.crud_model),
]