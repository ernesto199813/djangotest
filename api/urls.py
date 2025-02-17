# api/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('productos/', views.ProductoList.as_view(), name='producto-list'), # changed function name
    path('productos/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'), # Added second URL for details
    path('register/', views.register, name='register'), # URL /api/register/
]