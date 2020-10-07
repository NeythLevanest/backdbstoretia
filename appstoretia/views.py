from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from appstoretia.models import *
from appstoretia.serializers import *

class UsuariosViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class VentasViewSet(viewsets.ModelViewSet):
    serializer_class = VentasSerializer 
    queryset = Ventas.objects.all()

class CaracteristicasViewSet(viewsets.ModelViewSet):
    queryset = Caracteristicas.objects.all()
    serializer_class = VentasSerializer

class TiendasViewSet(viewsets.ModelViewSet):
    queryset = Tiendas.objects.all()
    serializer_class = TiendasSerializer