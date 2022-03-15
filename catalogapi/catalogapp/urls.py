from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('product/<str:sku>/', views.product),
]
