"""pantalla de login de SauceDemo."""

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import config

logger = logging.getLogger(__name__)


class LoginPage:
    URL = config.BASE_URL

    # Localizadores (prioridad: ID -> Name -> CSS corto -> XPath)
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.NAME, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.ESPERA_EXPLICITA)

    def abrir(self):
        """Carga la URL de login en el navegador."""
        logger.info("Abriendo %s", self.URL)
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario):
        """Escribe el nombre de usuario."""
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_clave(self, clave):
        """Escribe la contraseña."""
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)
        return self

    def hacer_clic_login(self):
        """Hace clic en el botón Login."""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login_completo(self, usuario=config.USUARIO_VALIDO, clave=config.CLAVE_VALIDA):
        """Completa usuario y contraseña y envía el formulario."""
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()
        logger.info("Login enviado con el usuario '%s'", usuario)
        return self

    def obtener_mensaje_error(self):
        """Devuelve el texto del mensaje de error de login."""
        return self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        ).text
