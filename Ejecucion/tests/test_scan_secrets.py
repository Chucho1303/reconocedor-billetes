import scan_secrets


def test_detecta_credenciales_hardcoded(tmp_path):
    clave = "sk-" + "a1B2c3D4e5F6g7H8i9J0k1L2"
    (tmp_path / "mal.py").write_text('API_KEY = "%s"\npassword = "supersecreta99"\n' % clave, encoding="utf-8")
    nombres = {h[2] for h in scan_secrets.escanear(tmp_path)}
    assert "Credencial asignada en codigo" in nombres and "Anthropic/OpenAI key" in nombres


def test_detecta_nombres_con_prefijo(tmp_path):
    (tmp_path / "mal.py").write_text('DB_PASSWORD = "hunter2hunter2"\nSTRIPE_SECRET_KEY = "abcdef123456"\n', encoding="utf-8")
    assert len(scan_secrets.escanear(tmp_path)) == 2


def test_acepta_variables_de_entorno(tmp_path):
    (tmp_path / "bien.py").write_text('import os\nAPI_KEY = os.environ["API_KEY"]\n', encoding="utf-8")
    assert scan_secrets.escanear(tmp_path) == []


def test_el_proyecto_no_tiene_secretos():
    assert scan_secrets.escanear(scan_secrets.Path(__file__).resolve().parents[2]) == []
