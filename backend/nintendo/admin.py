from django.contrib import admin
from .models import Consola, Videojuego, Personaje, Noticia, Evento, Pedido, DetallePedido

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_lanzamiento', 'precio', 'stock', 'es_actual')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion')
    list_filter = ('es_actual',)

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_lanzamiento', 'precio', 'stock', 'destacado')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'descripcion', 'desarrollador')
    list_filter = ('categoria', 'destacado', 'consolas')

class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'primera_aparicion', 'es_protagonista')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion', 'biografia')
    list_filter = ('es_protagonista',)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'autor', 'visualizaciones', 'es_destacada')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'contenido')
    list_filter = ('es_destacada', 'fecha_publicacion')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin', 'es_online')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion', 'ubicacion')
    list_filter = ('es_online',)

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'usuario', 'fecha_creacion', 'estado', 'total')
    search_fields = ('referencia', 'usuario__username', 'direccion_envio')
    list_filter = ('estado', 'fecha_creacion')
    inlines = [DetallePedidoInline]

# Register models
admin.site.register(Consola, ConsolaAdmin)
admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido)
