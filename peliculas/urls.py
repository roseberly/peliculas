from django.urls import path
from . import views 

from django.conf import settings 
from django.contrib.staticfiles.urls import static 

from django import forms 


urlpatterns = [
    path("", views.inicio, name="inicio"), 
    path("nosotros/", views.nosotros, name="nosotros"),
    path("peliculas/", views.peliculas, name="peliculas"),
    path("crear/", views.crear, name="crear"),
    path("eliminar/<int:id>/", views.eliminar, name="eliminar"),
    path("peliculas/editar/<int:id>/", views.editar, name="editar"),
    path('salir/', views.salir, name="salir"),
    path('aportar/', views.aportar, name="aportar"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
