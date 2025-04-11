from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .models import Consola, Videojuego, Personaje, Noticia, Evento, Pedido, DetallePedido
from .serializers import (
    UserSerializer, RegisterSerializer, ConsolaSerializer, VideojuegoSerializer, 
    PersonajeSerializer, NoticiaSerializer, EventoSerializer, PedidoSerializer, 
    DetallePedidoSerializer, VideojuegoDetailSerializer, PersonajeDetailSerializer,
    NoticiaDetailSerializer, PedidoDetailSerializer
)

# Authentication Views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

# User Views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

# Model ViewSets
class ConsolaViewSet(viewsets.ModelViewSet):
    queryset = Consola.objects.all()
    serializer_class = ConsolaSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VideojuegoDetailSerializer
        return VideojuegoSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def destacados(self, request):
        destacados = Videojuego.objects.filter(destacado=True)
        serializer = self.get_serializer(destacados, many=True)
        return Response(serializer.data)

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PersonajeDetailSerializer
        return PersonajeSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def protagonistas(self, request):
        protagonistas = Personaje.objects.filter(es_protagonista=True)
        serializer = self.get_serializer(protagonistas, many=True)
        return Response(serializer.data)

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NoticiaDetailSerializer
        return NoticiaSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
    
    @action(detail=True, methods=['post'])
    def register_view(self, request, slug=None):
        noticia = self.get_object()
        noticia.visualizaciones += 1
        noticia.save()
        return Response({'status': 'view registered'})

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Pedido.objects.all()
        return Pedido.objects.filter(usuario=user)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PedidoDetailSerializer
        return PedidoSerializer
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return DetallePedido.objects.all()
        return DetallePedido.objects.filter(pedido__usuario=user)
