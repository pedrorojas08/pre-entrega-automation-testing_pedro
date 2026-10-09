# Pre-Entrega: Automatización de Testing en SauceDemo

## Propósito del proyecto

Automatizar los flujos básicos de navegación del sitio [saucedemo.com](https://www.saucedemo.com) con Selenium WebDriver y Python, como pre-entrega del curso de Automatización QA.

Los casos de prueba son independientes entre sí:

| Archivo | Test | Qué valida |
|---------|------|------------|
| `test_login.py` | `test_login_exitoso` | Login con credenciales válidas, redirección a `/inventory.html`, título "Swag Labs" y sección "Products". |
| `test_add_to_cart.py` | `test_catalogo_inventario` | Título "Products", presencia de productos, nombre y precio del primero, y elementos de la interfaz (menú, filtro, carrito). |
| `test_add_to_cart.py` | `test_agregar_producto_al_carrito` | Agregar el primer producto, contador del carrito en 1 y producto listado en el carrito. |
| `test_checkout.py` | `test_checkout_completo` | Compra completa: carrito, datos del comprador, resumen y mensaje de confirmación. |

## Tecnologías utilizadas

- Python 3
- Pytest
- Selenium WebDriver 4 (Chrome)
- pytest-html (reporte HTML)
- Git y GitHub

## Estructura del proyecto

Se aplica el patrón Page Object Model: los localizadores y las acciones de cada pantalla viven en `pages/`, y los tests solo describen el flujo.

```
├── tests/
│   ├── test_login.py         # Login
│   ├── test_add_to_cart.py   # Catálogo y carrito
│   └── test_checkout.py      # Compra completa
├── pages/
│   ├── login_page.py         # Pantalla de login
│   ├── inventory_page.py     # Catálogo de productos
│   └── checkout_page.py      # Carrito y checkout
├── utils/
│   ├── driver_factory.py     # Creación y configuración de Chrome
│   └── config.py             # URL, credenciales, tiempos y carpetas
├── reports/                  # Reporte HTML y log de ejecución
├── screenshots/              # Capturas automáticas de los tests fallidos
├── conftest.py               # Fixture del navegador y captura ante fallos
├── requirements.txt          # Dependencias
└── pytest.ini                # Configuración de Pytest y de los logs
```

## Instalación de dependencias

Requisitos previos: Python y Google Chrome instalados. Selenium descarga el driver de Chrome automáticamente.

```bash
python -m venv venv
venv\Scripts\activate       
pip install -r requirements.txt
```

## Ejecución de las pruebas

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

## Reportes y evidencias

- `reports/reporte.html`: reporte HTML con el resultado de cada test.
- `reports/ejecucion.log`: log de la ejecución.
- `screenshots/`: capturas de pantalla que se guardan automáticamente cuando un test falla.
