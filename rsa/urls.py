from . import views
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]