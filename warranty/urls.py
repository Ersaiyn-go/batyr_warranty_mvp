from django.urls import path
from . import views

app_name = 'warranty'

urlpatterns = [
    path('', views.check_warranty, name='home'),
    path('warranty/', views.check_warranty, name='check'),
]
