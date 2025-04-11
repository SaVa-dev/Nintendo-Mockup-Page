from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, UserViewSet, ConsolaViewSet, VideojuegoViewSet, 
    PersonajeViewSet, NoticiaViewSet, EventoViewSet, PedidoViewSet, 
    DetallePedidoViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('consolas', ConsolaViewSet)
router.register('videojuegos', VideojuegoViewSet)
router.register('personajes', PersonajeViewSet)
router.register('noticias', NoticiaViewSet)
router.register('eventos', EventoViewSet)
router.register('pedidos', PedidoViewSet, basename='pedidos')
router.register('detalles-pedido', DetallePedidoViewSet, basename='detalles-pedido')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]