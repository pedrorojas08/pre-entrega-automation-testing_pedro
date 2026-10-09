"""Configuración general del proyecto: URL, credenciales, tiempos y carpetas."""

import os
from pathlib import Path

# Sitio bajo prueba
BASE_URL = "https://www.saucedemo.com/"

# Credenciales válidas de SauceDemo
USUARIO_VALIDO = "standard_user"
CLAVE_VALIDA = "secret_sauce"

# Datos de prueba para el formulario de checkout
NOMBRE_COMPRADOR = "Test"
APELLIDO_COMPRADOR = "Usuario"
CODIGO_POSTAL = "1000"

# Tiempos de espera en segundos
ESPERA_IMPLICITA = 5
ESPERA_EXPLICITA = 10

# Ejecutar con HEADLESS=1 para no mostrar la ventana del navegador
HEADLESS = os.getenv("HEADLESS") == "1"

# Carpetas de evidencias
RAIZ_PROYECTO = Path(__file__).parent.parent
CARPETA_SCREENSHOTS = RAIZ_PROYECTO / "screenshots"
