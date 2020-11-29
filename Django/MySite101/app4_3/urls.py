from django.urls import path
from . import views # 1

urlpatterns = [
    path('getvalue1', views.getvalue_1),
    path('getvalue2/<full_name>/<address>', views.getvalue_2),
    path('display_form1', views.display_form1),# Display Web Form
    path('display_form2', views.display_form2),# Display Web Form
    path('getvalue3', views.getvalue_3),
]