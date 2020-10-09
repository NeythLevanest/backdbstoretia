from rest_framework import serializers
from appstoretia.models import Usuario, Tiendas, Caracteristicas, Ventas


class UsuarioSerializer (serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Usuario
        fields = '__all__'

class TiendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiendas
        fields = '__all__'

class CaracteristicasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Caracteristicas
        fields = '__all__'

class VentasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'
