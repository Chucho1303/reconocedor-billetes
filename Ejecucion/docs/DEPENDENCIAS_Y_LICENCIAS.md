# Gestión de dependencias y licencias

Documento del punto **8. Gestión de Dependencias y Licencias**. Última auditoría: 2026-11-09
(Python 3.12, versiones de `requirements.lock.txt`).

## 1. Política

| Categoría | Licencias | Decisión |
|---|---|---|
| Permisivas | MIT, BSD-2/3, Apache-2.0, PSF-2.0, ISC, Zlib, 0BSD, CC0, MIT-CMU | ✅ Permitidas |
| Copyleft débil | MPL-2.0 | ⚠️ Permitida solo **sin modificar** el paquete |
| Copyleft fuerte / restrictivas | GPL, AGPL, LGPL (como dependencia propia), SSPL, propietarias / comerciales | ❌ Prohibidas sin revisión legal |

La política se hace cumplir automáticamente con `python Ejecucion/scripts/check_licenses.py` (falla con
código 1 si aparece una licencia prohibida o desconocida) y en el job **security** del CI.

## 2. Dependencias fijadas (repetibilidad)

- `requirements.txt`: 3 dependencias directas con versión exacta (`==`).
- `requirements.lock.txt`: árbol completo de 35 paquetes de ejecución.
- `requirements-dev.txt`: pruebas y auditoría (no entran a la imagen Docker).

## 3. Obsolescencia y mantenimiento

- Al momento de la auditoría **todas** las dependencias estaban en su última versión publicada
  (`pip list --outdated` no reportó ninguna, salvo la herramienta `pip` misma).
- `.github/dependabot.yml` abre cada semana PRs para pip, Docker y GitHub Actions.
- `pip-audit -r Ejecucion/requirements.lock.txt` (en CI) consulta la base de vulnerabilidades de PyPI.
  Resultado de la auditoría: **No known vulnerabilities found**.
- Ninguna dependencia está abandonada: todas son proyectos activos con lanzamientos recientes.

## 4. Inventario de licencias (ejecución)

| Paquete | Versión | Licencia | Tipo | Sitio |
|---|---|---|---|---|
| altair | 6.3.0 | BSD License | transitiva | https://github.com/vega/altair |
| anyio | 4.16.0 | MIT | transitiva | https://anyio.readthedocs.io/en/stable/versionhistory.html |
| attrs | 26.1.0 | MIT | transitiva | https://www.attrs.org/en/stable/changelog.html |
| certifi | 2026.10.23 | Mozilla Public License 2.0 (MPL 2.0) | transitiva | https://github.com/certifi/python-certifi |
| charset-normalizer | 3.5.2 | MIT | transitiva | https://github.com/jawah/charset_normalizer/blob/master/CHANGELOG.md |
| click | 8.5.1 | BSD-3-Clause | transitiva | https://github.com/pallets/click/ |
| h11 | 0.16.0 | MIT License | transitiva | https://github.com/python-hyper/h11 |
| idna | 3.20 | BSD-3-Clause | transitiva | https://github.com/kjd/idna |
| itsdangerous | 2.2.0 | BSD License | transitiva | https://github.com/pallets/itsdangerous/ |
| Jinja2 | 3.1.6 | BSD License | transitiva | https://github.com/pallets/jinja/ |
| jsonschema | 4.26.0 | MIT | transitiva | https://github.com/python-jsonschema/jsonschema |
| jsonschema-specifications | 2025.9.1 | MIT | transitiva | https://github.com/python-jsonschema/jsonschema-specifications |
| MarkupSafe | 3.0.4 | BSD-3-Clause | transitiva | https://github.com/pallets/markupsafe/ |
| narwhals | 2.28.0 | MIT | transitiva | https://github.com/narwhals-dev/narwhals |
| numpy | 2.5.4 | BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 | directa | https://numpy.org |
| opencv-python-headless | 5.0.0.93 | Apache Software License | directa | https://github.com/opencv/opencv-python |
| packaging | 26.3 | Apache-2.0 OR BSD-2-Clause | transitiva | https://github.com/pypa/packaging |
| pandas | 3.1.1 | BSD-3-Clause | transitiva | https://pandas.pydata.org |
| pillow | 13.0.0 | MIT-CMU | transitiva | https://python-pillow.org |
| protobuf | 7.36.2 | 3-Clause BSD License | transitiva | https://developers.google.com/protocol-buffers/ |
| pyarrow | 26.0.1 | Apache-2.0 | transitiva | https://arrow.apache.org/ |
| pydeck | 0.9.3 | Apache License 2.0 | transitiva | https://github.com/visgl/deck.gl/tree/master/bindings/pydeck |
| python-dateutil | 4.0.0 | BSD-3-Clause | transitiva | https://github.com/dateutil/dateutil |
| python-multipart | 0.0.33 | Apache-2.0 | transitiva | https://github.com/Kludex/python-multipart |
| referencing | 0.37.0 | MIT | transitiva | https://github.com/python-jsonschema/referencing |
| requests | 2.34.2 | Apache Software License | transitiva | https://github.com/psf/requests |
| rpds-py | 2026.9.1 | MIT | transitiva | https://github.com/crate-py/rpds |
| starlette | 1.10.0 | BSD-3-Clause | transitiva | https://github.com/Kludex/starlette |
| streamlit | 1.67.0 | Apache-2.0 | directa | https://streamlit.io |
| typing_extensions | 4.16.0 | PSF-2.0 | transitiva | https://github.com/python/typing_extensions |
| tzdata | 2026.6 | Apache-2.0 | transitiva | https://github.com/python/tzdata |
| urllib3 | 2.8.0 | MIT | transitiva | https://github.com/urllib3/urllib3/blob/main/CHANGES.rst |
| uvicorn | 0.54.0 | BSD-3-Clause | transitiva | https://uvicorn.dev/ |
| watchdog | 7.1.0 | Apache-2.0 | transitiva | https://github.com/gorakhargosh/watchdog |
| websockets | 17.4 | BSD-3-Clause | transitiva | https://github.com/python-websockets/websockets |

Resultado: **0 licencias prohibidas**. Hallazgos a tener en cuenta:

- **certifi — MPL-2.0**: copyleft débil por archivo. Se usa tal cual, sin modificarlo, por lo que no
  impone obligaciones sobre el código del proyecto.
- **opencv-python-headless — Apache-2.0**: el paquete incluye bibliotecas de FFmpeg
  (`libavcodec`, `libavformat`, `libavutil`), cuyo aviso de terceros está en
  `LICENSE-3RD-PARTY.txt` del wheel. FFmpeg se distribuye bajo LGPL-2.1 y viene enlazado de forma
  dinámica (archivos `.so` separados); este proyecto no los modifica. Si el producto se distribuyera
  comercialmente hay que conservar ese aviso, y conviene confirmarlo con asesoría legal.
- **numpy** — combinación BSD-3-Clause, 0BSD, MIT, Zlib y CC0-1.0: todas permisivas.

## 5. Licencia del proyecto

El código propio se publica bajo **MIT** (ver `LICENSE`), compatible con todas las dependencias anteriores.

## 6. Cómo repetir la auditoría

```bash
pip install -r Ejecucion/requirements-dev.txt
python Ejecucion/scripts/check_licenses.py                         # política de licencias
python Ejecucion/scripts/check_licenses.py --markdown licencias.md # tabla actualizada
pip-audit -r Ejecucion/requirements.lock.txt                       # vulnerabilidades
pip list --outdated                                      # versiones nuevas
```
