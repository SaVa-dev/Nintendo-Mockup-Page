from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='consolas/', null=True, blank=True)
    es_actual = models.BooleanField(default=True)
    especificaciones = models.JSONField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Consolas"
    
    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    CATEGORIAS = [
        ('ACT', 'Acción'),
        ('AVT', 'Aventura'),
        ('RPG', 'RPG'),
        ('DEP', 'Deportes'),
        ('FGT', 'Lucha'),
        ('PZL', 'Puzzle'),
        ('SIM', 'Simulación'),
        ('PLT', 'Plataformas'),
        ('FAM', 'Familiar'),
    ]
    
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=3, choices=CATEGORIAS)
    fecha_lanzamiento = models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    consolas = models.ManyToManyField(Consola, related_name='videojuegos')
    editor = models.CharField(max_length=100, default='Nintendo')
    desarrollador = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='videojuegos/')
    calificacion_edad = models.CharField(max_length=5, default='E')
    stock = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    primera_aparicion = models.ForeignKey(Videojuego, on_delete=models.SET_NULL, null=True, related_name='personajes_introducidos')
    imagen = models.ImageField(upload_to='personajes/')
    biografia = models.TextField(blank=True)
    es_protagonista = models.BooleanField(default=False)
    videojuegos = models.ManyToManyField(Videojuego, related_name='personajes')
    
    class Meta:
        verbose_name_plural = "Personajes"
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='noticias/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuegos_relacionados = models.ManyToManyField(Videojuego, related_name='noticias', blank=True)
    consolas_relacionadas = models.ManyToManyField(Consola, related_name='noticias', blank=True)
    visualizaciones = models.PositiveIntegerField(default=0)
    es_destacada = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion = models.CharField(max_length=200, blank=True)
    es_online = models.BooleanField(default=True)
    enlace_stream = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='eventos/')
    videojuegos_presentados = models.ManyToManyField(Videojuego, related_name='eventos', blank=True)
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ('PEN', 'Pendiente'),
        ('PAG', 'Pagado'),
        ('ENV', 'Enviado'),
        ('ENT', 'Entregado'),
        ('CAN', 'Cancelado'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=3, choices=ESTADOS, default='PEN')
    direccion_envio = models.TextField()
    metodo_pago = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    referencia = models.CharField(max_length=20, unique=True)
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    videojuego = models.ForeignKey(Videojuego, on_delete=models.SET_NULL, null=True, blank=True)
    consola = models.ForeignKey(Consola, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        producto = self.videojuego.titulo if self.videojuego else self.consola.nombre
        return f"{producto} x{self.cantidad}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.precio_unitario * self.cantidad
        super().save(*args, **kwargs)