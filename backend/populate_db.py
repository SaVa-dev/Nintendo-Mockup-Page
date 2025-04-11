# save_as: populate_db.py

import os
import django
import random
import uuid
from datetime import datetime, timedelta
from decimal import Decimal

# Configurar entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files import File
from nintendo.models import Consola, Videojuego, Personaje, Noticia, Evento, Pedido, DetallePedido

# Crear superusuario si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superusuario 'admin' creado con contraseña 'admin123'")

# Crear usuario normal para pruebas
if not User.objects.filter(username='usuario').exists():
    User.objects.create_user('usuario', 'usuario@example.com', 'usuario123')
    print("Usuario 'usuario' creado con contraseña 'usuario123'")

# --- CONSOLAS ---
consolas_data = [
    {
        'nombre': 'Nintendo Switch',
        'slug': 'nintendo-switch',
        'fecha_lanzamiento': '2017-03-03',
        'descripcion': 'Consola híbrida que permite jugar tanto en el televisor como en modo portátil.',
        'precio': 299.99,
        'stock': 100,
        'es_actual': True,
        'especificaciones': {
            'procesador': 'NVIDIA Tegra X1',
            'memoria': '4GB RAM',
            'almacenamiento': '32GB',
            'pantalla': 'LCD táctil 6.2 pulgadas, 720p'
        }
    },
    {
        'nombre': 'Nintendo Switch Lite',
        'slug': 'nintendo-switch-lite',
        'fecha_lanzamiento': '2019-09-20',
        'descripcion': 'Versión compacta y exclusivamente portátil de Nintendo Switch.',
        'precio': 199.99,
        'stock': 150,
        'es_actual': True,
        'especificaciones': {
            'procesador': 'NVIDIA Tegra X1',
            'memoria': '4GB RAM',
            'almacenamiento': '32GB',
            'pantalla': 'LCD táctil 5.5 pulgadas, 720p'
        }
    },
    {
        'nombre': 'Nintendo Switch OLED',
        'slug': 'nintendo-switch-oled',
        'fecha_lanzamiento': '2021-10-08',
        'descripcion': 'Modelo mejorado con pantalla OLED de mayor tamaño y soporte ajustable.',
        'precio': 349.99,
        'stock': 80,
        'es_actual': True,
        'especificaciones': {
            'procesador': 'NVIDIA Tegra X1',
            'memoria': '4GB RAM',
            'almacenamiento': '64GB',
            'pantalla': 'OLED táctil 7 pulgadas, 720p'
        }
    },
    {
        'nombre': 'Nintendo 3DS',
        'slug': 'nintendo-3ds',
        'fecha_lanzamiento': '2011-02-26',
        'descripcion': 'Consola portátil con capacidad para mostrar efectos 3D sin necesidad de gafas especiales.',
        'precio': 149.99,
        'stock': 20,
        'es_actual': False,
        'especificaciones': {
            'procesador': 'ARM11 MPCore dual-core',
            'memoria': '128MB RAM',
            'almacenamiento': '2GB',
            'pantalla': 'LCD superior 3.53 pulgadas (3D), LCD táctil inferior 3.02 pulgadas'
        }
    },
    {
        'nombre': 'Nintendo Wii U',
        'slug': 'nintendo-wii-u',
        'fecha_lanzamiento': '2012-11-18',
        'descripcion': 'Consola de sobremesa con un controlador principal con pantalla integrada.',
        'precio': 199.99,
        'stock': 10,
        'es_actual': False,
        'especificaciones': {
            'procesador': 'IBM PowerPC tri-core',
            'memoria': '2GB RAM',
            'almacenamiento': '32GB',
            'gamepad': 'Controlador con pantalla LCD táctil de 6.2 pulgadas'
        }
    }
]

# Eliminar datos existentes (opcional, comenta estas líneas si no quieres borrar datos)
print("Limpiando datos existentes...")
DetallePedido.objects.all().delete()
Pedido.objects.all().delete()
Evento.objects.all().delete()
Noticia.objects.all().delete()
Personaje.objects.all().delete()
Videojuego.objects.all().delete()
Consola.objects.all().delete()

# Insertar consolas
print("Creando consolas...")
consolas_creadas = {}
for consola_data in consolas_data:
    consola = Consola.objects.create(
        nombre=consola_data['nombre'],
        slug=consola_data['slug'],
        fecha_lanzamiento=consola_data['fecha_lanzamiento'],
        descripcion=consola_data['descripcion'],
        precio=consola_data['precio'],
        stock=consola_data['stock'],
        es_actual=consola_data['es_actual'],
        especificaciones=consola_data['especificaciones']
    )
    consolas_creadas[consola_data['nombre']] = consola
    print(f"Creada consola: {consola.nombre}")

# --- VIDEOJUEGOS ---
videojuegos_data = [
    {
        'titulo': 'The Legend of Zelda: Breath of the Wild',
        'slug': 'zelda-breath-of-the-wild',
        'descripcion': 'Aventura de acción en un vasto mundo abierto que revoluciona la serie Zelda.',
        'categoria': 'AVT',
        'fecha_lanzamiento': '2017-03-03',
        'precio': 59.99,
        'consolas': ['Nintendo Switch', 'Nintendo Wii U'],
        'editor': 'Nintendo',
        'desarrollador': 'Nintendo EPD',
        'calificacion_edad': 'E10+',
        'stock': 50,
        'destacado': True
    },
    {
        'titulo': 'Super Mario Odyssey',
        'slug': 'super-mario-odyssey',
        'descripcion': 'Mario se embarca en un viaje alrededor del mundo para salvar a la princesa Peach.',
        'categoria': 'PLT',
        'fecha_lanzamiento': '2017-10-27',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Nintendo EPD',
        'calificacion_edad': 'E10+',
        'stock': 45,
        'destacado': True
    },
    {
        'titulo': 'Animal Crossing: New Horizons',
        'slug': 'animal-crossing-new-horizons',
        'descripcion': 'Simulador de vida donde construyes tu propia isla desierta y la desarrollas.',
        'categoria': 'SIM',
        'fecha_lanzamiento': '2020-03-20',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Nintendo EPD',
        'calificacion_edad': 'E',
        'stock': 60,
        'destacado': True
    },
    {
        'titulo': 'Mario Kart 8 Deluxe',
        'slug': 'mario-kart-8-deluxe',
        'descripcion': 'El juego de carreras definitivo con todos tus personajes favoritos de Nintendo.',
        'categoria': 'DEP',
        'fecha_lanzamiento': '2017-04-28',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Nintendo EAD',
        'calificacion_edad': 'E',
        'stock': 55,
        'destacado': True
    },
    {
        'titulo': 'Pokémon Escarlata y Púrpura',
        'slug': 'pokemon-escarlata-purpura',
        'descripcion': 'La primera aventura Pokémon de mundo abierto donde exploras la región de Paldea.',
        'categoria': 'RPG',
        'fecha_lanzamiento': '2022-11-18',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Game Freak',
        'calificacion_edad': 'E',
        'stock': 70,
        'destacado': True
    },
    {
        'titulo': 'Splatoon 3',
        'slug': 'splatoon-3',
        'descripcion': 'Shooter en tercera persona donde disparas tinta para marcar territorio.',
        'categoria': 'ACT',
        'fecha_lanzamiento': '2022-09-09',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Nintendo EPD',
        'calificacion_edad': 'E10+',
        'stock': 40,
        'destacado': False
    },
    {
        'titulo': 'Super Smash Bros. Ultimate',
        'slug': 'super-smash-bros-ultimate',
        'descripcion': 'Juego de lucha con todos los personajes que han aparecido en la serie.',
        'categoria': 'FGT',
        'fecha_lanzamiento': '2018-12-07',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Sora Ltd./Bandai Namco Studios',
        'calificacion_edad': 'E10+',
        'stock': 35,
        'destacado': True
    },
    {
        'titulo': 'Fire Emblem: Three Houses',
        'slug': 'fire-emblem-three-houses',
        'descripcion': 'RPG táctico con una historia dividida en tres casas nobles.',
        'categoria': 'RPG',
        'fecha_lanzamiento': '2019-07-26',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Intelligent Systems/Koei Tecmo',
        'calificacion_edad': 'T',
        'stock': 25,
        'destacado': False
    },
    {
        'titulo': 'Luigi\'s Mansion 3',
        'slug': 'luigis-mansion-3',
        'descripcion': 'Luigi debe rescatar a Mario y amigos de un hotel encantado.',
        'categoria': 'AVT',
        'fecha_lanzamiento': '2019-10-31',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Next Level Games',
        'calificacion_edad': 'E',
        'stock': 30,
        'destacado': False
    },
    {
        'titulo': 'Pokémon Leyendas: Arceus',
        'slug': 'pokemon-leyendas-arceus',
        'descripcion': 'Aventura Pokémon ambientada en el pasado de la región de Sinnoh.',
        'categoria': 'RPG',
        'fecha_lanzamiento': '2022-01-28',
        'precio': 59.99,
        'consolas': ['Nintendo Switch'],
        'editor': 'Nintendo',
        'desarrollador': 'Game Freak',
        'calificacion_edad': 'E',
        'stock': 42,
        'destacado': False
    }
]

# Insertar videojuegos
print("Creando videojuegos...")
videojuegos_creados = {}
for videojuego_data in videojuegos_data:
    videojuego = Videojuego.objects.create(
        titulo=videojuego_data['titulo'],
        slug=videojuego_data['slug'],
        descripcion=videojuego_data['descripcion'],
        categoria=videojuego_data['categoria'],
        fecha_lanzamiento=videojuego_data['fecha_lanzamiento'],
        precio=videojuego_data['precio'],
        editor=videojuego_data['editor'],
        desarrollador=videojuego_data['desarrollador'],
        calificacion_edad=videojuego_data['calificacion_edad'],
        stock=videojuego_data['stock'],
        destacado=videojuego_data['destacado'],
    )
    
    # Añadir consolas al videojuego
    for consola_nombre in videojuego_data['consolas']:
        if consola_nombre in consolas_creadas:
            videojuego.consolas.add(consolas_creadas[consola_nombre])
    
    videojuegos_creados[videojuego_data['titulo']] = videojuego
    print(f"Creado videojuego: {videojuego.titulo}")

# --- PERSONAJES ---
personajes_data = [
    {
        'nombre': 'Mario',
        'slug': 'mario',
        'descripcion': 'El fontanero italiano más famoso del mundo de los videojuegos.',
        'primera_aparicion': 'Super Mario Odyssey',  # Usaremos este como referencia aunque no sea su primera aparición real
        'biografia': 'Mario es un fontanero italiano que se ha convertido en el héroe del Reino Champiñón, rescatando a la Princesa Peach de las garras de Bowser en numerosas ocasiones.',
        'es_protagonista': True,
        'videojuegos': ['Super Mario Odyssey', 'Mario Kart 8 Deluxe', 'Super Smash Bros. Ultimate']
    },
    {
        'nombre': 'Link',
        'slug': 'link',
        'descripcion': 'El héroe silencioso de Hyrule que empuña la Espada Maestra.',
        'primera_aparicion': 'The Legend of Zelda: Breath of the Wild',  # Referencia, no es su primera aparición real
        'biografia': 'Link es un joven guerrero destinado a salvar el reino de Hyrule y a la princesa Zelda de las fuerzas del mal, principalmente de Ganon.',
        'es_protagonista': True,
        'videojuegos': ['The Legend of Zelda: Breath of the Wild', 'Super Smash Bros. Ultimate']
    },
    {
        'nombre': 'Princesa Peach',
        'slug': 'princesa-peach',
        'descripcion': 'La gobernante del Reino Champiñón y frecuente objetivo de secuestros por parte de Bowser.',
        'primera_aparicion': 'Super Mario Odyssey',  # Referencia
        'biografia': 'La Princesa Peach es la soberana del Reino Champiñón. A pesar de ser secuestrada con frecuencia, ha demostrado en varias ocasiones ser una gobernante capaz y una aventurera valiente.',
        'es_protagonista': False,
        'videojuegos': ['Super Mario Odyssey', 'Mario Kart 8 Deluxe', 'Super Smash Bros. Ultimate']
    },
    {
        'nombre': 'Inkling',
        'slug': 'inkling',
        'descripcion': 'Criaturas que pueden cambiar entre forma humanoide y forma de calamar.',
        'primera_aparicion': 'Splatoon 3',  # Referencia
        'biografia': 'Los Inklings son criaturas con la habilidad de transformarse entre formas humanoide y calamar. Compiten en batallas territoriales disparando tinta.',
        'es_protagonista': True,
        'videojuegos': ['Splatoon 3', 'Super Smash Bros. Ultimate']
    },
    {
        'nombre': 'Pikachu',
        'slug': 'pikachu',
        'descripcion': 'El Pokémon eléctrico más reconocible y mascota de la franquicia.',
        'primera_aparicion': 'Pokémon Escarlata y Púrpura',  # Referencia
        'biografia': 'Pikachu es un Pokémon de tipo Eléctrico conocido por sus mejillas rojas que almacenan electricidad. Es la mascota oficial de la franquicia Pokémon.',
        'es_protagonista': False,
        'videojuegos': ['Pokémon Escarlata y Púrpura', 'Pokémon Leyendas: Arceus', 'Super Smash Bros. Ultimate']
    }
]

# Insertar personajes
print("Creando personajes...")
for personaje_data in personajes_data:
    # Obtener el videojuego de primera aparición
    primera_aparicion = videojuegos_creados.get(personaje_data['primera_aparicion'])
    
    personaje = Personaje.objects.create(
        nombre=personaje_data['nombre'],
        slug=personaje_data['slug'],
        descripcion=personaje_data['descripcion'],
        primera_aparicion=primera_aparicion,
        biografia=personaje_data['biografia'],
        es_protagonista=personaje_data['es_protagonista']
    )
    
    # Añadir videojuegos relacionados
    for videojuego_titulo in personaje_data['videojuegos']:
        if videojuego_titulo in videojuegos_creados:
            personaje.videojuegos.add(videojuegos_creados[videojuego_titulo])
    
    print(f"Creado personaje: {personaje.nombre}")

# --- NOTICIAS ---
noticias_data = [
    {
        'titulo': 'Anunciado nuevo DLC para Animal Crossing: New Horizons',
        'slug': 'dlc-animal-crossing-new-horizons',
        'contenido': 'Nintendo ha anunciado un nuevo DLC para Animal Crossing: New Horizons que incluirá nuevas islas para explorar, personajes y objetos decorativos. El DLC estará disponible a partir del próximo mes.',
        'fecha_publicacion': timezone.now() - timedelta(days=5),
        'videojuegos_relacionados': ['Animal Crossing: New Horizons'],
        'consolas_relacionadas': ['Nintendo Switch'],
        'visualizaciones': 1250,
        'es_destacada': True
    },
    {
        'titulo': 'The Legend of Zelda: Breath of the Wild 2 se retrasa hasta 2025',
        'slug': 'zelda-botw-2-retraso',
        'contenido': 'Nintendo ha confirmado que la esperada secuela de Breath of the Wild necesitará más tiempo de desarrollo para cumplir con las expectativas. La nueva fecha de lanzamiento se sitúa en primavera de 2025.',
        'fecha_publicacion': timezone.now() - timedelta(days=10),
        'videojuegos_relacionados': ['The Legend of Zelda: Breath of the Wild'],
        'consolas_relacionadas': ['Nintendo Switch'],
        'visualizaciones': 3500,
        'es_destacada': True
    },
    {
        'titulo': 'Revelados nuevos personajes para Super Smash Bros. Ultimate',
        'slug': 'nuevos-personajes-smash-ultimate',
        'contenido': 'El director Masahiro Sakurai ha revelado que se añadirán dos nuevos personajes sorpresa a Super Smash Bros. Ultimate como parte de una actualización gratuita. Los detalles se anunciarán en un Nintendo Direct próximamente.',
        'fecha_publicacion': timezone.now() - timedelta(days=15),
        'videojuegos_relacionados': ['Super Smash Bros. Ultimate'],
        'consolas_relacionadas': ['Nintendo Switch'],
        'visualizaciones': 2800,
        'es_destacada': False
    },
    {
        'titulo': 'Nintendo anuncia nueva versión de Switch con mejor batería',
        'slug': 'nueva-switch-mejor-bateria',
        'contenido': 'Una nueva revisión de Nintendo Switch llegará a las tiendas el próximo trimestre, ofreciendo hasta 8 horas de batería, una mejora significativa respecto a los modelos actuales.',
        'fecha_publicacion': timezone.now() - timedelta(days=20),
        'consolas_relacionadas': ['Nintendo Switch'],
        'visualizaciones': 1900,
        'es_destacada': False
    },
    {
        'titulo': 'Splatoon 3 alcanza los 10 millones de copias vendidas',
        'slug': 'splatoon-3-diez-millones-ventas',
        'contenido': 'Nintendo ha anunciado que Splatoon 3 ha superado los 10 millones de copias vendidas en todo el mundo, convirtiéndose en uno de los juegos más exitosos de la consola Switch.',
        'fecha_publicacion': timezone.now() - timedelta(days=25),
        'videojuegos_relacionados': ['Splatoon 3'],
        'consolas_relacionadas': ['Nintendo Switch'],
        'visualizaciones': 1500,
        'es_destacada': False
    }
]

# Insertar noticias
print("Creando noticias...")
admin_user = User.objects.get(username='admin')
for noticia_data in noticias_data:
    noticia = Noticia.objects.create(
        titulo=noticia_data['titulo'],
        slug=noticia_data['slug'],
        contenido=noticia_data['contenido'],
        fecha_publicacion=noticia_data['fecha_publicacion'],
        autor=admin_user,
        visualizaciones=noticia_data['visualizaciones'],
        es_destacada=noticia_data['es_destacada']
    )
    
    # Añadir videojuegos relacionados
    if 'videojuegos_relacionados' in noticia_data:
        for videojuego_titulo in noticia_data['videojuegos_relacionados']:
            if videojuego_titulo in videojuegos_creados:
                noticia.videojuegos_relacionados.add(videojuegos_creados[videojuego_titulo])
    
    # Añadir consolas relacionadas
    if 'consolas_relacionadas' in noticia_data:
        for consola_nombre in noticia_data['consolas_relacionadas']:
            if consola_nombre in consolas_creadas:
                noticia.consolas_relacionadas.add(consolas_creadas[consola_nombre])
    
    print(f"Creada noticia: {noticia.titulo}")

# --- EVENTOS ---
eventos_data = [
    {
        'nombre': 'Nintendo Direct: E3 2024',
        'slug': 'nintendo-direct-e3-2024',
        'descripcion': 'Presentación digital con los próximos lanzamientos de Nintendo para la segunda mitad de 2024.',
        'fecha_inicio': timezone.now() + timedelta(days=45),
        'fecha_fin': timezone.now() + timedelta(days=45, hours=1),
        'es_online': True,
        'enlace_stream': 'https://www.youtube.com/nintendo',
        'videojuegos_presentados': ['Mario Kart 8 Deluxe', 'Super Smash Bros. Ultimate', 'Splatoon 3']
    },
    {
        'nombre': 'Torneo Mundial de Pokémon 2024',
        'slug': 'torneo-mundial-pokemon-2024',
        'descripcion': 'Competición oficial de los juegos de Pokémon con jugadores de todo el mundo.',
        'fecha_inicio': timezone.now() + timedelta(days=90),
        'fecha_fin': timezone.now() + timedelta(days=93),
        'ubicacion': 'Tokyo, Japón',
        'es_online': False,
        'enlace_stream': 'https://www.twitch.tv/pokemon',
        'videojuegos_presentados': ['Pokémon Escarlata y Púrpura']
    },
    {
        'nombre': 'Nintendo Treehouse Live: Zelda Special',
        'slug': 'nintendo-treehouse-zelda',
        'descripcion': 'Jornada especial dedicada a las novedades de la saga The Legend of Zelda.',
        'fecha_inicio': timezone.now() + timedelta(days=30),
        'fecha_fin': timezone.now() + timedelta(days=30, hours=3),
        'es_online': True,
        'enlace_stream': 'https://www.youtube.com/nintendo',
        'videojuegos_presentados': ['The Legend of Zelda: Breath of the Wild']
    },
    {
        'nombre': 'Super Nintendo World: Apertura Europa',
        'slug': 'super-nintendo-world-europa',
        'descripcion': 'Inauguración oficial de la zona temática de Nintendo en Universal Studios Europa.',
        'fecha_inicio': timezone.now() + timedelta(days=180),
        'fecha_fin': timezone.now() + timedelta(days=180),
        'ubicacion': 'Barcelona, España',
        'es_online': False,
        'videojuegos_presentados': ['Super Mario Odyssey', 'Mario Kart 8 Deluxe']
    }
]

# Insertar eventos
print("Creando eventos...")
for evento_data in eventos_data:
    evento = Evento.objects.create(
        nombre=evento_data['nombre'],
        slug=evento_data['slug'],
        descripcion=evento_data['descripcion'],
        fecha_inicio=evento_data['fecha_inicio'],
        fecha_fin=evento_data['fecha_fin'],
        es_online=evento_data['es_online'],
        ubicacion=evento_data.get('ubicacion', ''),
        enlace_stream=evento_data.get('enlace_stream', '')
    )
    
    # Añadir videojuegos presentados
    if 'videojuegos_presentados' in evento_data:
        for videojuego_titulo in evento_data['videojuegos_presentados']:
            if videojuego_titulo in videojuegos_creados:
                evento.videojuegos_presentados.add(videojuegos_creados[videojuego_titulo])
    
    print(f"Creado evento: {evento.nombre}")

# --- PEDIDOS Y DETALLES DE PEDIDO ---
# Crear pedidos de ejemplo
print("Creando pedidos y detalles...")
usuario = User.objects.get(username='usuario')
admin = User.objects.get(username='admin')

for i in range(1, 6):
    # Crear pedido para usuario normal
    pedido_usuario = Pedido.objects.create(
        usuario=usuario,
        fecha_creacion=timezone.now() - timedelta(days=i*3),
        estado=random.choice(['PEN', 'PAG', 'ENV', 'ENT']),
        direccion_envio=f'Calle Ejemplo {i}, Ciudad Ejemplo, 28000',
        metodo_pago='Tarjeta de crédito',
        total=Decimal('0'),  # Se calculará después
        referencia=f'PED-{uuid.uuid4().hex[:8].upper()}',
        notas=f'Pedido de prueba #{i}'
    )
    
    # Crear pedido para admin
    if i <= 3:
        pedido_admin = Pedido.objects.create(
            usuario=admin,
            fecha_creacion=timezone.now() - timedelta(days=i*5),
            estado=random.choice(['PEN', 'PAG', 'ENV', 'ENT']),
            direccion_envio=f'Avenida Admin {i}, Ciudad Admin, 28001',
            metodo_pago='PayPal',
            total=Decimal('0'),  # Se calculará después
            referencia=f'ADM-{uuid.uuid4().hex[:8].upper()}',
            notas=f'Pedido de administrador #{i}'
        )
    
    # Añadir detalles a pedido de usuario
    total_usuario = Decimal('0')
    for _ in range(1, random.randint(2, 5)):
        # Seleccionar un producto aleatorio (videojuego o consola)
        producto_tipo = random.choice(['videojuego', 'consola'])
        if producto_tipo == 'videojuego':
            producto = random.choice(list(videojuegos_creados.values()))
            precio = producto.precio
            detalle = DetallePedido.objects.create(
                pedido=pedido_usuario,
                videojuego=producto,
                cantidad=random.randint(1, 3),
                precio_unitario=precio
            )
        else:
            producto = random.choice(list(consolas_creadas.values()))
            precio = producto.precio
            detalle = DetallePedido.objects.create(
                pedido=pedido_usuario,
                consola=producto,
                cantidad=random.randint(1, 2),
                precio_unitario=precio
            )
        # Usar Decimal explícitamente
        total_usuario += Decimal(str(detalle.subtotal))
    
    # Actualizar total del pedido de usuario
    pedido_usuario.total = total_usuario
    pedido_usuario.save()
    print(f"Creado pedido para usuario: {pedido_usuario.referencia} - Total: {total_usuario}")
    
    # Añadir detalles a pedido de admin si existe
    if i <= 3:
        total_admin = Decimal('0')
        for _ in range(1, random.randint(1, 3)):
            producto_tipo = random.choice(['videojuego', 'consola'])
            if producto_tipo == 'videojuego':
                producto = random.choice(list(videojuegos_creados.values()))
                precio = producto.precio
                detalle = DetallePedido.objects.create(
                    pedido=pedido_admin,
                    videojuego=producto,
                    cantidad=random.randint(1, 2),
                    precio_unitario=precio
                )
            else:
                producto = random.choice(list(consolas_creadas.values()))
                precio = producto.precio
                detalle = DetallePedido.objects.create(
                    pedido=pedido_admin,
                    consola=producto,
                    cantidad=1,
                    precio_unitario=precio
                )
            # Usar Decimal explícitamente aquí también
            total_admin += Decimal(str(detalle.subtotal))
        
        pedido_admin.total = total_admin
        pedido_admin.save()
        print(f"Creado pedido para admin: {pedido_admin.referencia} - Total: {total_admin}")

print("\nBase de datos poblada exitosamente!")
print("Usuarios creados:")
print("- admin (admin123) - Superusuario")
print("- usuario (usuario123) - Usuario normal")