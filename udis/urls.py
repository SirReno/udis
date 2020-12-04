from django.urls import path
from . import views

app_name = "udis"
urlpatterns = [
    path('', views.home, name='home'),
    path('udis/', views.udis, name='udis'),
    path('dollars/', views.dollars, name='dollars')
]