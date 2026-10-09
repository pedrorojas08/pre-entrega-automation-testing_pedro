"""Casos de prueba del catálogo y del carrito de SauceDemo."""

import logging

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_catalogo_inventario(driver):
    """El inventario muestra el título, los productos y los elementos de la interfaz."""
    LoginPage(driver).abrir().login_completo()
    inventario = InventoryPage(driver).esperar_carga()

    # Título de la página
    assert inventario.obtener_titulo() == "Products", "Título de sección incorrecto"

    # Debe haber al menos un producto visible
    cantidad = inventario.contar_productos()
    assert cantidad > 0, "No se encontraron productos visibles en el inventario"

    # Nombre y precio del primer producto
    nombre = inventario.obtener_nombre_primer_producto()
    precio = inventario.obtener_precio_primer_producto()
    assert nombre != "", "El primer producto no tiene nombre"
    assert precio.startswith("$"), f"Precio con formato inesperado: {precio}"
    logger.info("Productos: %d. Primero: %s (%s)", cantidad, nombre, precio)

    # Elementos importantes de la interfaz
    assert inventario.esta_menu_visible(), "Falta el botón del menú"
    assert inventario.esta_filtro_visible(), "Falta el filtro de orden"
    assert inventario.esta_carrito_visible(), "Falta el ícono del carrito"


def test_agregar_producto_al_carrito(driver):
    """Al agregar un producto, el contador sube a 1 y el producto aparece en el carrito."""
    LoginPage(driver).abrir().login_completo()
    inventario = InventoryPage(driver).esperar_carga()

    nombre_agregado = inventario.agregar_primer_producto()

    # Espera explícita del badge del carrito
    contador = inventario.obtener_contador_carrito()
    assert contador == 1, f"El contador debería mostrar 1, pero muestra {contador}"

    carrito = inventario.ir_al_carrito()
    assert "/cart.html" in driver.current_url, "No se navegó al carrito"
    assert carrito.contar_productos() == 1, "El carrito debería tener un solo producto"
    assert nombre_agregado in carrito.obtener_nombres_productos(), (
        f"'{nombre_agregado}' no aparece en el carrito"
    )
    logger.info("Producto verificado en el carrito: %s", nombre_agregado)
