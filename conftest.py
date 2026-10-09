"""Configuraciónavegador y capturas ante fallos."""

import logging
from datetime import datetime

import pytest

from utils import config
from utils.driver_factory import crear_driver

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    """Abre un Chrome nuevo para cada test y lo cierra al terminar."""
    navegador = crear_driver()

    yield navegador

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda una captura de pantalla en screenshots/ si el test falla."""
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver")
        if navegador is not None:
            config.CARPETA_SCREENSHOTS.mkdir(exist_ok=True)
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            archivo = config.CARPETA_SCREENSHOTS / f"{item.name}_{fecha}.png"
            navegador.save_screenshot(str(archivo))
            logger.error("Test fallido: %s. Captura guardada en %s", item.name, archivo)
