
# 1. IMPORTACIONES

import os
from datetime import datetime

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for
)

from data import CATEGORIAS, PRODUCTOS


# 2. CONFIGURACIÓN DE LA APLICACIÓN

app = Flask(__name__)

# Clave utilizada por Flask para proteger las sesiones y los mensajes.
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "cambiar-en-produccion"
)


# 3. ROLES DISPONIBLES PARA EL REGISTRO

# Estos roles pueden crear una cuenta desde la página web.
# El administrador se crea directamente desde la base de datos.

ROLES_REGISTRO = [
    {
        "slug": "cliente",
        "nombre": "Cliente",
        "desc": "Compra tus fritos favoritos",
        "icono": "bi-cart3",
        "rf": "RF-01.1"
    },
    {
        "slug": "vendedor",
        "nombre": "Vendedor",
        "desc": "Publica tus productos",
        "icono": "bi-shop",
        "rf": "RF-01.5"
    },
    {
        "slug": "domiciliario",
        "nombre": "Domiciliario",
        "desc": "Haz entregas y genera ingresos",
        "icono": "bi-bicycle",
        "rf": "RF-01.6"
    }
]


# 4. FILTRO PARA FORMATEAR PRECIOS EN PESOS COLOMBIANOS

@app.template_filter("cop")
def formato_cop(valor):
    """
    Convierte un número en un precio con formato colombiano.

    Ejemplo:
    2500 -> $2.500
    """
    return "$" + f"{valor:,.0f}".replace(",", ".")


# 5. VARIABLES GLOBALES PARA LAS PLANTILLAS HTML

@app.context_processor
def variables_globales():
    # Permite utilizar {{ anio }} en las plantillas HTML.
    return {
        "anio": datetime.now().year
    }


# 6. PÁGINA PRINCIPAL

@app.route("/")
def index():
    # Envía las categorías y los productos al archivo index.html.
    return render_template(
        "index.html",
        categorias=CATEGORIAS,
        productos=PRODUCTOS
    )


# 7. PÁGINA PARA EXPLORAR PRODUCTOS

@app.route("/explorar")
def explorar():
    # Obtener la categoría seleccionada desde la URL.
    slug = request.args.get("categoria", "").strip()

    # Buscar la categoría correspondiente.
    categoria = next(
        (c for c in CATEGORIAS if c["slug"] == slug),
        None
    )

    # Si la categoría no existe, mostrar error 404.
    if slug and categoria is None:
        abort(404)

    # Mostrar todos los productos o solamente los de esa categoría.
    productos = [
        p for p in PRODUCTOS
        if not categoria or p["categoria"] == slug
    ]

    # Enviar los datos a explorar.html.
    return render_template(
        "explorar.html",
        categorias=CATEGORIAS,
        productos=productos,
        activa=slug
    )



# ============================================================
# 8. SELECCIONAR UN ROL
# ============================================================

@app.route("/iniciar-sesion")
def iniciar_sesion():
    return render_template(
        "seleccionar_rol.html",
        roles=ROLES_REGISTRO
    )


# ============================================================
# 9. PÁGINA DE INICIO DE SESIÓN
# ============================================================

@app.route("/acceso/<rol>", methods=["GET", "POST"])
def acceso_rol(rol):

    # Buscar el rol seleccionado.
    rol_actual = next(
        (r for r in ROLES_REGISTRO if r["slug"] == rol),
        None
    )

    if rol_actual is None:
        abort(404)

    # Procesar el formulario de inicio de sesión.
    if request.method == "POST":

        correo = request.form.get(
            "correo", ""
        ).strip().lower()

        clave = request.form.get("clave", "")

        if not correo or not clave:
            flash(
                "Escribe tu correo y tu contraseña.",
                "danger"
            )
        else:
            # Pendiente: verificar los datos en la base de datos.
            flash(
                "El inicio de sesión todavía no está conectado "
                "a la base de datos.",
                "info"
            )

        return redirect(url_for("acceso_rol", rol=rol))

    # Mostrar únicamente el formulario para iniciar sesión.
    return render_template(
        "auth.html",
        rol=rol_actual
    )


# ============================================================
# 10. PÁGINA DE REGISTRO
# ============================================================

@app.route("/registro")
def registro():
    # Primero se debe seleccionar un rol.
    return redirect(url_for("iniciar_sesion"))


@app.route("/registro/<rol>", methods=["GET", "POST"])
def registro_rol(rol):

    # Buscar el rol seleccionado.
    rol_actual = next(
        (r for r in ROLES_REGISTRO if r["slug"] == rol),
        None
    )

    if rol_actual is None:
        abort(404)

    # Procesar el formulario de registro.
    if request.method == "POST":

        nombre = request.form.get(
            "nombre", ""
        ).strip()

        correo = request.form.get(
            "correo", ""
        ).strip().lower()

        clave = request.form.get("clave", "")

        confirmar_clave = request.form.get(
            "confirmar_clave", ""
        )

        if not nombre or not correo or not clave or not confirmar_clave:
            flash(
                "Completa todos los campos.",
                "danger"
            )

        elif clave != confirmar_clave:
            flash(
                "Las contraseñas no coinciden.",
                "danger"
            )

        elif len(clave) < 8:
            flash(
                "La contraseña debe tener al menos 8 caracteres.",
                "danger"
            )

        else:
            # Pendiente: guardar el usuario en la base de datos.
            flash(
                "El formulario está completo, pero todavía "
                "falta conectar el registro a la base de datos.",
                "info"
            )

        return redirect(url_for("registro_rol", rol=rol))

    # Mostrar únicamente el formulario de registro.
    return render_template(
        "registro.html",
        rol=rol_actual
    )


# 10. PÁGINAS QUE TODAVÍA ESTÁN PENDIENTES

PROXIMAMENTE = {
    "vender": (
        "Vender con FRITOS TECH",
        "RF-01.5"
    ),
    "recuperar-contrasena": (
        "Recuperar contraseña",
        "RF-01.3"
    )
}


@app.route("/<pagina>")
def proximamente(pagina):

    # Comprobar si la página solicitada está registrada.
    if pagina not in PROXIMAMENTE:
        abort(404)

    # Obtener el título y el requisito funcional.
    titulo, rf = PROXIMAMENTE[pagina]

    # Mostrar la pantalla de función pendiente.
    return render_template(
        "proximamente.html",
        titulo=titulo,
        rf=rf
    )


# 11. MANEJO DE PÁGINAS NO ENCONTRADAS

@app.errorhandler(404)
def no_encontrada(_):

    # Mostrar una página personalizada cuando una ruta no existe.
    return render_template(
        "proximamente.html",
        titulo="No encontramos esa página",
        rf=None
    ), 404


# 12. EJECUTAR LA APLICACIÓN

if __name__ == "__main__":
    app.run(debug=True)
