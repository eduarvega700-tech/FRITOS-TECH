# 1. DATOS DE EJEMPLO

"""
Datos de ejemplo para mostrar las categorías y los productos
en la página principal de FRITOS TECH.

Por ahora, los datos están escritos directamente en Python.
Cuando conectemos la base de datos, se reemplazarán por
consultas a las tablas categoria y producto.
"""


# 2. CATEGORÍAS DE PRODUCTOS

CATEGORIAS = [
    {
        "nombre": "Empanadas",
        "slug": "empanadas",
        "imagen": "empanadas.png"
    },
    {
        "nombre": "Arepas de huevo",
        "slug": "arepas-de-huevo",
        "imagen": "arepas.png"
    },
    {
        "nombre": "Carimañolas",
        "slug": "carimañola",
        "imagen": "carimañola.png"
    },
    {
        "nombre": "Patacones",
        "slug": "patacones",
        "imagen": "patacones.png"
    },
    {
        "nombre": "Buñuelos",
        "slug": "buñuelos",
        "imagen": "buñuelos.png"
    },
    {
        "nombre": "Otros",
        "slug": "otros",
        "imagen": "otros.png"
    }
]

# 3. CIUDAD DE LOS PRODUCTOS

# Variable que reutilizamos para no escribir la ciudad
# repetidamente en cada producto.

_CIUDAD = "Cartagena, Bolívar"


# 4. LISTA DE PRODUCTOS DE EJEMPLO

PRODUCTOS = [


    # PRODUCTO 1: EMPANADAS DE CARNE


    {
        "id": 1,
        "nombre": "Empanadas de carne",
        "vendedor": "La Delicia de la Abuela",
        "rating": 4.8,
        "resenas": 124,
        "ciudad": _CIUDAD,
        "precio": 2000,
        "etiqueta": "Más vendido",
        "categoria": "empanadas",
        "emoji": "",
        "img": "prod-empanadas.jpg"
    },


    # PRODUCTO 2: AREPA DE HUEVO

    {
        "id": 2,
        "nombre": "Arepa de huevo",
        "vendedor": "Sabor Caribe",
        "rating": 4.9,
        "resenas": 98,
        "ciudad": _CIUDAD,
        "precio": 3000,
        "etiqueta": "Nuevo",
        "categoria": "arepas-de-huevo",
        "emoji": "",
        "img": "prod-arepa.jpg"
    },


    # PRODUCTO 3: CARIMAÑOLAS DE YUCA


    {
        "id": 3,
        "nombre": "Carimañolas de yuca",
        "vendedor": "El Sabor del Caribe",
        "rating": 4.7,
        "resenas": 76,
        "ciudad": _CIUDAD,
        "precio": 2500,
        "etiqueta": "Más vendido",
        "categoria": "carimañolas",
        "emoji": "",
        "img": "prod-carimañola.jpg"
    },

    # PRODUCTO 4: PATACONES CON HOGAO

    {
        "id": 4,
        "nombre": "Patacones con hogao",
        "vendedor": "La Esquina del Sabor",
        "rating": 4.8,
        "resenas": 110,
        "ciudad": _CIUDAD,
        "precio": 3500,
        "etiqueta": "Popular",
        "categoria": "patacones",
        "emoji": "",
        "img": "prod-patacones.jpg"
    },

    # PRODUCTO 5: BUÑUELOS DE FRÍJOL

    {
        "id": 5,
        "nombre": "Buñuelos",
        "vendedor": "Doña Rosa Fritos",
        "rating": 4.6,
        "resenas": 52,
        "ciudad": _CIUDAD,
        "precio": 1500,
        "etiqueta": None,
        "categoria": "buñuelos",
        "emoji": "",
        "img": "prod-buñuelos.jpg"
    },

    # PRODUCTO 6: EMPANADA DE POLLO

    {
        "id": 6,
        "nombre": "Empanada de pollo",
        "vendedor": "El Rincón Cartagenero",
        "rating": 4.7,
        "resenas": 88,
        "ciudad": _CIUDAD,
        "precio": 2000,
        "etiqueta": None,
        "categoria": "empanadas",
        "emoji": "",
        "img": "prod-empanada-pollo.jpg"
    },

    # PRODUCTO 7: AREPA DE HUEVO ESPECIAL

    {
        "id": 7,
        "nombre": "Arepa de huevo especial",
        "vendedor": "La Matrona",
        "rating": 4.8,
        "resenas": 64,
        "ciudad": _CIUDAD,
        "precio": 3500,
        "etiqueta": None,
        "categoria": "arepas-de-huevo",
        "emoji": "",
        "img": "prod-arepa-especial.jpg"
    },

    # PRODUCTO 8: PATACÓN CON QUESO

    {
        "id": 8,
        "nombre": "Patacón con queso",
        "vendedor": "Fritos Don Luis",
        "rating": 4.5,
        "resenas": 41,
        "ciudad": _CIUDAD,
        "precio": 3000,
        "etiqueta": None,
        "categoria": "patacones",
        "emoji": "",
        "img": "prod-patacon-queso.jpg"
    }

]