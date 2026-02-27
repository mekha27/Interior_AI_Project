from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test/', views.test_api),
    path('upload/', views.upload_image),
]