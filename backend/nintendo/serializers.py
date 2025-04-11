from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Consola, Videojuego, Personaje, Noticia, Evento, Pedido, DetallePedido

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = '__all__'

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = '__all__'

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.ReadOnlyField(source='autor.username')
    
    class Meta:
        model = Noticia
        fields = '__all__'
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        
class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'

class VideojuegoDetailSerializer(serializers.ModelSerializer):
    consolas = ConsolaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Videojuego
        fields = '__all__'

class PersonajeDetailSerializer(serializers.ModelSerializer):
    primera_aparicion = VideojuegoSerializer(read_only=True)
    videojuegos = VideojuegoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Personaje
        fields = '__all__'

class NoticiaDetailSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)
    videojuegos_relacionados = VideojuegoSerializer(many=True, read_only=True)
    consolas_relacionadas = ConsolaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Noticia
        fields = '__all__'

class PedidoDetailSerializer(serializers.ModelSerializer):
    detalles = serializers.SerializerMethodField()
    usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Pedido
        fields = '__all__'
    
    def get_detalles(self, obj):
        detalles = DetallePedido.objects.filter(pedido=obj)
        return DetallePedidoSerializer(detalles, many=True).data