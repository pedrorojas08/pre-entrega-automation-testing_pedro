"""Fábrica del WebDriver: centraliza la creación y configuración de Chrome."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import config


def crear_driver():
    """Crea y devuelve un Chrome configurado para los tests."""
    opciones = Options()
    opciones.add_argument("--window-size=1366,900")
    # Evita el aviso de Chrome sobre contraseñas filtradas, que tapa la página
    opciones.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    if config.HEADLESS:
        opciones.add_argument("--headless=new")

    driver = webdriver.Chrome(options=opciones)
    driver.implicitly_wait(config.ESPERA_IMPLICITA)
    return driver
