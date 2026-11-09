"""Pruebas con DATOS REALES: fotos de ejemplo y plantillas incluidas en el repositorio."""
from pathlib import Path

import cv2
import numpy as np
import pytest

import billetes

RAIZ = Path(__file__).resolve().parent.parent
EJEMPLOS = RAIZ / "Front" / "ejemplos"


@pytest.fixture(scope="module")
def plantillas():
    return billetes.cargar_plantillas()


def reconocer(ruta, plantillas):
    img = cv2.imread(str(ruta))
    assert img is not None, "no se pudo leer %s" % ruta
    recorte, _, _ = billetes.segmentar(img)
    return billetes.clasificar(recorte, plantillas)


def test_plantillas_disponibles(plantillas):
    assert {p["den"] for p in plantillas} == {20, 50, 1000}


def test_foto_real_de_1000(plantillas):
    den, conf, _ = reconocer(EJEMPLOS / "Mil-pesos.jpg", plantillas)
    assert den == 1000 and conf >= 0.9


def test_foto_real_de_50(plantillas):
    den, conf, _ = reconocer(EJEMPLOS / "captura_01.jpg", plantillas)
    assert den == 50 and conf >= billetes.UMBRAL_ACEPTACION


def test_foto_vertical_no_falla_y_devuelve_puntajes_validos(plantillas):
    den, conf, detalle = reconocer(EJEMPLOS / "billete_50_vertical.jpg", plantillas)
    assert den in (None, 50)
    assert 0.0 <= conf <= 1.0 and set(detalle) == {20, 50, 1000}


@pytest.mark.parametrize("den", [20, 50, 1000])
def test_cada_plantilla_se_reconoce_a_si_misma(den, plantillas):
    for archivo in billetes.listar_imagenes(str(Path(billetes.CARPETA_PLANTILLAS) / str(den))):
        assert reconocer(archivo, plantillas)[0] == den


def test_ruido_no_se_reconoce_como_billete(plantillas):
    rng = np.random.default_rng(0)
    ruido = rng.integers(0, 255, (280, 600, 3), dtype=np.uint8)
    assert billetes.clasificar(ruido, plantillas)[0] is None


def test_sin_plantillas_lanza_error():
    with pytest.raises(RuntimeError):
        billetes.clasificar(np.zeros((280, 600, 3), np.uint8), [])


def test_etiqueta():
    assert billetes.etiqueta(None, 0.1) == "No reconocido"
    assert billetes.etiqueta(500, 0.876) == "$500 MXN (88%)"
