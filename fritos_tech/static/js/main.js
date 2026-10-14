
(function () {
    "use strict";

    /* =====================================================
       1. CONFIGURACIÓN DEL CARRITO
    ===================================================== */

    // Clave utilizada para guardar el carrito en el navegador.
    var CLAVE = "fritosTechCarrito";


    /* =====================================================
       2. LEER Y GUARDAR EL CARRITO
    ===================================================== */

    // Obtener los productos guardados.
    function leer() {
        try {
            return JSON.parse(localStorage.getItem(CLAVE)) || {};
        } catch (e) {
            return {};
        }
    }

    // Guardar los productos en el navegador.
    function guardar(carrito) {
        try {
            localStorage.setItem(CLAVE, JSON.stringify(carrito));
        } catch (e) {
            // Continúa funcionando aunque el almacenamiento no esté disponible.
        }
    }

    // Calcular la cantidad total de productos.
    function total(carrito) {
        return Object.keys(carrito).reduce(function (suma, id) {
            return suma + carrito[id];
        }, 0);
    }


    /* =====================================================
       3. CONTADOR DEL CARRITO
    ===================================================== */

    var contador = document.getElementById("cart-count");

    // Actualizar el número que aparece en el carrito.
    function pintarContador() {
        var cantidad = total(leer());

        if (!contador) {
            return;
        }

        contador.textContent = cantidad;
        contador.hidden = cantidad === 0;
    }


    /* =====================================================
       4. SISTEMA DE AVISOS
    ===================================================== */

    var aviso = document.getElementById("aviso");
    var temporizador;

    // Mostrar un mensaje temporal en pantalla.
    function mostrarAviso(texto) {
        if (!aviso) {
            return;
        }

        aviso.textContent = texto;
        aviso.classList.add("aviso--visible");

        // Reiniciar el tiempo si ya había un aviso.
        clearTimeout(temporizador);

        temporizador = setTimeout(function () {
            aviso.classList.remove("aviso--visible");
        }, 2200);
    }


    /* =====================================================
       5. EVENTOS GENERALES DE LA PÁGINA
    ===================================================== */

    document.addEventListener("click", function (e) {

        /* -----------------------------------------------
           5.1. AGREGAR PRODUCTOS AL CARRITO
        ----------------------------------------------- */

        var agregar = e.target.closest("[data-add]");

        if (agregar) {
            var carrito = leer();
            var id = agregar.getAttribute("data-add");

            // Sumar una unidad del producto seleccionado.
            carrito[id] = (carrito[id] || 0) + 1;

            guardar(carrito);
            pintarContador();

            // Mostrar la confirmación.
            var nombre = agregar.getAttribute("data-nombre");

            mostrarAviso(
                (nombre || "Producto") + " agregado al carrito"
            );

            return;
        }


        /* -----------------------------------------------
           5.2. MARCAR O DESMARCAR FAVORITOS
        ----------------------------------------------- */

        var favorito = e.target.closest(".btn-fav");

        if (favorito) {
            var activo = favorito.getAttribute("aria-pressed") === "true";

            favorito.setAttribute(
                "aria-pressed",
                String(!activo)
            );

            return;
        }


        /* -----------------------------------------------
           5.3. MOSTRAR U OCULTAR CONTRASEÑAS
        ----------------------------------------------- */

        var ver = e.target.closest("[data-ver-clave]");

        if (ver) {
            var campo = document.getElementById(
                ver.getAttribute("data-ver-clave")
            );

            // Comprobar que el campo exista.
            if (!campo) {
                return;
            }

            var visible = campo.type === "text";

            // Cambiar el tipo del campo.
            campo.type = visible ? "password" : "text";

            // Actualizar el estado accesible del botón.
            ver.setAttribute(
                "aria-pressed",
                String(!visible)
            );

            ver.setAttribute(
                "aria-label",
                visible ? "Mostrar contraseña" : "Ocultar contraseña"
            );

            // Cambiar el icono de Bootstrap Icons.
            if (ver.firstElementChild) {
                ver.firstElementChild.className = visible
                    ? "bi bi-eye-slash"
                    : "bi bi-eye";
            }

            return;
        }


        /* -----------------------------------------------
           5.4. BOTONES DE FUNCIONES PRÓXIMAS
        ----------------------------------------------- */

        if (e.target.closest("[data-proximamente]")) {
            mostrarAviso("Próximamente");
            return;
        }


        /* -----------------------------------------------
           5.5. CONSULTAR EL CARRITO
        ----------------------------------------------- */

        if (e.target.closest("#btn-carrito")) {
            var cantidad = total(leer());

            if (cantidad > 0) {
                mostrarAviso(
                    "Tienes " + cantidad +
                    (cantidad === 1
                        ? " producto"
                        : " productos") +
                    " en el carrito"
                );
            } else {
                mostrarAviso("Tu carrito está vacío");
            }
        }

    });


    /* =====================================================
       6. FILTRO DE PRODUCTOS POPULARES
    ===================================================== */

    var grilla = document.getElementById("grilla-populares");

    // Ejecutar el filtro solo si existe la grilla.
    if (grilla) {

        // Obtener los productos que contiene la grilla.
        var items = Array.prototype.slice.call(grilla.children);

        // Obtener los botones de filtro.
        var chips = document.querySelectorAll("[data-filtro]");

        // Mensaje para cuando no haya resultados.
        var vacio = document.getElementById("sin-resultados");

        // Máximo de productos visibles.
        var MAXIMO = 4;


        /* -----------------------------------------------
           6.1. FILTRAR LOS PRODUCTOS
        ----------------------------------------------- */

        function filtrar(slug) {
            var visibles = 0;

            items.forEach(function (producto) {

                // Comprobar si pertenece a la categoría seleccionada.
                var coincide =
                    slug === "todos" ||
                    producto.getAttribute("data-categoria") === slug;

                // Mostrar como máximo cuatro productos.
                var mostrar = coincide && visibles < MAXIMO;

                if (mostrar) {
                    visibles++;
                }

                // Ocultar los productos que no coinciden.
                producto.classList.toggle("d-none", !mostrar);
            });

            // Mostrar el mensaje si no hay resultados.
            if (vacio) {
                vacio.hidden = visibles > 0;
            }
        }


        /* -----------------------------------------------
           6.2. EVENTOS DE LOS BOTONES DE FILTRO
        ----------------------------------------------- */

        chips.forEach(function (chip) {

            chip.addEventListener("click", function () {

                // Actualizar cuál filtro está seleccionado.
                chips.forEach(function (otroChip) {
                    var seleccionado = otroChip === chip;

                    otroChip.classList.toggle(
                        "chip--activo",
                        seleccionado
                    );

                    otroChip.setAttribute(
                        "aria-pressed",
                        String(seleccionado)
                    );
                });

                // Filtrar por la categoría seleccionada.
                filtrar(chip.getAttribute("data-filtro"));
            });

        });


        /* -----------------------------------------------
           6.3. FILTRO INICIAL
        ----------------------------------------------- */

        // Mostrar todos los productos al cargar la página,
        // respetando el límite máximo de cuatro.
        filtrar("todos");
    }


    /* =====================================================
       7. INICIALIZACIÓN
    ===================================================== */

    // Actualizar el contador al cargar el JavaScript.
    pintarContador();

})();
