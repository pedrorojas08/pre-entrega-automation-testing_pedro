"""carrito y del proceso de checkout."""

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import config

logger = logging.getLogger(__name__)


class CheckoutPage:
    # Carrito
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    # Formulario con los datos del comprador
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    # Resumen y confirmación
    _FINISH_BUTTON = (By.ID, "finish")
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.ESPERA_EXPLICITA)
        # Verifica que estamos en la página del carrito
        self.wait.until(EC.url_contains("/cart.html"))

    def obtener_nombres_productos(self):
        """Devuelve los nombres de los productos listados."""
        elementos = self.driver.find_elements(*self._ITEM_NAMES)
        return [elemento.text for elemento in elementos]

    def contar_productos(self):
        """Devuelve la cantidad de productos en el carrito."""
        return len(self.driver.find_elements(*self._CART_ITEMS))

    def iniciar_checkout(self):
        """Hace clic en Checkout y espera el formulario de datos."""
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        self.wait.until(EC.url_contains("/checkout-step-one.html"))
        return self

    def completar_datos(self, nombre, apellido, codigo_postal):
        """Completa los datos del comprador y continúa al resumen."""
        self.wait.until(
            EC.visibility_of_element_located(self._FIRST_NAME)
        ).send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self._POSTAL_CODE).send_keys(codigo_postal)
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
        self.wait.until(EC.url_contains("/checkout-step-two.html"))
        logger.info("Datos del comprador completados")
        return self

    def finalizar_compra(self):
        """Hace clic en Finish y espera la página de confirmación."""
        self.driver.find_element(*self._FINISH_BUTTON).click()
        self.wait.until(EC.url_contains("/checkout-complete.html"))
        logger.info("Compra finalizada")
        return self

    def obtener_mensaje_confirmacion(self):
        """Devuelve el encabezado de la página de compra completada."""
        return self.wait.until(
            EC.visibility_of_element_located(self._COMPLETE_HEADER)
        ).text
