"""La configuracion sale del entorno y tolera valores invalidos."""
import importlib

import billetes_config as cfg


def recargar():
    return importlib.reload(cfg)


def test_umbral_desde_entorno(monkeypatch):
    monkeypatch.setenv("BILLETES_UMBRAL", "0.5")
    assert recargar().UMBRAL_ACEPTACION == 0.5


def test_umbral_invalido_usa_defecto(monkeypatch):
    for malo in ("abc", "7", "-1", ""):
        monkeypatch.setenv("BILLETES_UMBRAL", malo)
        assert recargar().UMBRAL_ACEPTACION == 0.35


def test_equipo_desde_entorno(monkeypatch):
    monkeypatch.setenv("BILLETES_EQUIPO", "Ana; Luis ;")
    assert recargar().EQUIPO == ["Ana", "Luis"]


def test_dotenv_no_pisa_variables_existentes(tmp_path, monkeypatch):
    archivo = tmp_path / ".env"
    archivo.write_text("# comentario\nPRUEBA_A=desde_archivo\nPRUEBA_B='con comillas'\n", encoding="utf-8")
    monkeypatch.setenv("PRUEBA_A", "ya_definida")
    monkeypatch.delenv("PRUEBA_B", raising=False)
    cfg._cargar_dotenv(archivo)
    import os
    assert os.environ["PRUEBA_A"] == "ya_definida"
    assert os.environ["PRUEBA_B"] == "con comillas"
    monkeypatch.delenv("PRUEBA_B", raising=False)
    recargar()
