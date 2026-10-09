"""Caso de prueba del flujo completo de compra en SauceDemo."""

import logging

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import config

logger = logging.getLogger(__name__)


def test_checkout_completo(driver):
    """Un usuario agrega un producto y completa la compra hasta la confirmación."""
    LoginPage(driver).abrir().login_completo()
    inventario = InventoryPage(driver).esperar_carga()

    nombre_agregado = inventario.agregar_primer_producto()
    checkout = inventario.ir_al_carrito()
    assert nombre_agregado in checkout.obtener_nombres_productos(), (
        f"'{nombre_agregado}' no aparece en el carrito"
    )

    checkout.iniciar_checkout()
    checkout.completar_datos(
        config.NOMBRE_COMPRADOR, config.APELLIDO_COMPRADOR, config.CODIGO_POSTAL
    )

    # El resumen debe seguir mostrando el producto elegido
    assert nombre_agregado in checkout.obtener_nombres_productos(), (
        f"'{nombre_agregado}' no aparece en el resumen de la compra"
    )

    checkout.finalizar_compra()
    mensaje = checkout.obtener_mensaje_confirmacion()
    assert mensaje == "Thank you for your order!", f"Confirmación inesperada: {mensaje}"
    logger.info("Compra completada: %s", mensaje)
