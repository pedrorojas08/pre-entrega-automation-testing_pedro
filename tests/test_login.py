"""Casos de prueba del login de SauceDemo."""

import logging

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_login_exitoso(driver):
    """Un usuario válido ingresa y es redirigido al inventario."""
    LoginPage(driver).abrir().login_completo()

    # Espera explícita de la redirección al inventario
    inventario = InventoryPage(driver).esperar_carga()

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    assert driver.title == "Swag Labs", f"Título inesperado: {driver.title}"
    assert inventario.obtener_titulo() == "Products", "No aparece el título 'Products'"
    logger.info("Login exitoso, URL actual: %s", driver.current_url)
