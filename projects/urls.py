from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet
from . import views

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
] + router.urls