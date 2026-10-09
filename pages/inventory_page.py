"""página de inventario (catálogo de productos)."""

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import config

logger = logging.getLogger(__name__)


class InventoryPage:
    _TITLE = (By.CSS_SELECTOR, ".header_secondary_container .title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _SORT_FILTER = (By.CLASS_NAME, "product_sort_container")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.ESPERA_EXPLICITA)

    def esperar_carga(self):
        """Espera explícita hasta que la URL sea la del inventario."""
        self.wait.until(EC.url_contains("/inventory.html"))
        return self

    def obtener_titulo(self):
        """Devuelve el título de la sección (debería ser 'Products')."""
        return self.wait.until(EC.visibility_of_element_located(self._TITLE)).text

    def contar_productos(self):
        """Devuelve la cantidad de productos visibles en el catálogo."""
        self.wait.until(EC.visibility_of_element_located(self._PRODUCTS))
        productos = self.driver.find_elements(*self._PRODUCTS)
        return len([producto for producto in productos if producto.is_displayed()])

    def obtener_nombre_primer_producto(self):
        """Devuelve el nombre del primer producto del catálogo."""
        return self.driver.find_elements(*self._PRODUCT_NAME)[0].text

    def obtener_precio_primer_producto(self):
        """Devuelve el precio del primer producto del catálogo."""
        return self.driver.find_elements(*self._PRODUCT_PRICE)[0].text

    def esta_menu_visible(self):
        """Indica si el botón del menú hamburguesa está visible."""
        return self.driver.find_element(*self._MENU_BUTTON).is_displayed()

    def esta_filtro_visible(self):
        """Indica si el selector de orden de productos está visible."""
        return self.driver.find_element(*self._SORT_FILTER).is_displayed()

    def esta_carrito_visible(self):
        """Indica si el ícono del carrito está visible."""
        return self.driver.find_element(*self._CART_LINK).is_displayed()

    def agregar_primer_producto(self):
        """Agrega el primer producto al carrito y devuelve su nombre."""
        nombre = self.obtener_nombre_primer_producto()
        self.driver.find_elements(*self._ADD_BUTTONS)[0].click()
        logger.info("Producto agregado al carrito: %s", nombre)
        return nombre

    def obtener_contador_carrito(self):
        """Espera el badge del carrito y devuelve el número que muestra."""
        badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
        return int(badge.text)

    def ir_al_carrito(self):
        """Navega al carrito de compras."""
        self.driver.find_element(*self._CART_LINK).click()
        # Importación local para evitar dependencias circulares
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
