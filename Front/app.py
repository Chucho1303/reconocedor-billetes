"""Interfaz web del reconocedor de billetes mexicanos (Streamlit + OpenCV).

Reutiliza el algoritmo de ``billetes.py``: segmenta el billete, lo clasifica y
muestra el resultado, los puntajes y la imagen rectificada.
"""
from pathlib import Path
import sys

# Permite importar el motor ubicado en la carpeta Back.
ROOT_DIR = Path(__file__).resolve().parent.parent
BACK_DIR = ROOT_DIR / "Back"
sys.path.insert(0, str(BACK_DIR))

import billetes_config as cfg  # noqa: E402  (debe ir antes que cv2)

import cv2  # noqa: E402
import numpy as np  # noqa: E402
import streamlit as st  # noqa: E402
import streamlit.components.v1 as components  # noqa: E402

import billetes  # noqa: E402

BASE_DIR = Path(__file__).resolve().parent
EJEMPLOS = sorted(p for p in (BASE_DIR / "ejemplos").glob("*")
                  if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"))
EQUIPO = cfg.EQUIPO   # se define con la variable de entorno BILLETES_EQUIPO (nombres separados por ;)
GRUPO = cfg.GRUPO     # se define con BILLETES_GRUPO

st.set_page_config(page_title="Reconocedor de billetes mexicanos", page_icon="💵", layout="wide")

# Evita que el traductor del navegador convierta "$20" en "20 dólares".
try:
    components.html(
        """<script>
        try {
          const d = window.parent.document;
          d.documentElement.lang = 'es';
          d.documentElement.setAttribute('translate', 'no');
          if (!d.querySelector('meta[name=google]')) {
            const m = d.createElement('meta'); m.name = 'google'; m.content = 'notranslate'; d.head.appendChild(m);
          }
        } catch (e) {}
        </script>""",
        height=0,
    )
except Exception:
    pass

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    html, body, [class*="st-"], .stMarkdown {font-family: 'Poppins', sans-serif;}

    /* ================= FONDO ANIMADO ================= */
    .stApp {background: #020403 !important;}
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp > header {background: transparent !important;}
    .block-container {position: relative; z-index: 2; padding-top: 1.4rem; max-width: 1200px;}

    /* Aurora que se mueve */
    .stApp::before {content: ""; position: fixed; inset: -25%; z-index: 0; pointer-events: none; filter: blur(46px);
        background:
          radial-gradient(circle at 18% 28%, rgba(0,230,118,.34), transparent 38%),
          radial-gradient(circle at 82% 18%, rgba(0,184,212,.28), transparent 38%),
          radial-gradient(circle at 62% 82%, rgba(124,77,255,.26), transparent 40%),
          radial-gradient(circle at 12% 85%, rgba(0,200,83,.22), transparent 36%);
        animation: aurora 16s ease-in-out infinite alternate;}
    @keyframes aurora {
        0%   {transform: translate(0,0) scale(1) rotate(0deg);}
        50%  {transform: translate(6%,4%) scale(1.15) rotate(7deg);}
        100% {transform: translate(-6%,-5%) scale(1.06) rotate(-7deg);}}

    /* Cuadricula tecnologica en movimiento */
    .stApp::after {content: ""; position: fixed; inset: 0; z-index: 1; pointer-events: none;
        background-image: linear-gradient(rgba(0,230,118,.07) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0,230,118,.07) 1px, transparent 1px);
        background-size: 52px 52px;
        -webkit-mask-image: radial-gradient(ellipse at 50% 25%, #000 10%, transparent 75%);
                mask-image: radial-gradient(ellipse at 50% 25%, #000 10%, transparent 75%);
        animation: rejilla 22s linear infinite;}
    @keyframes rejilla {from {background-position: 0 0, 0 0;} to {background-position: 0 52px, 52px 0;}}

    /* Billetes flotando */
    .flotantes {position: fixed; inset: 0; z-index: 1; pointer-events: none; overflow: hidden;}
    .flotantes span {position: absolute; bottom: -80px; font-size: 2.6rem; opacity: 0; filter: blur(.4px);
                     animation: sube 16s linear infinite;}
    .flotantes span:nth-child(1) {left: 6%;  animation-duration: 17s; animation-delay: 0s;}
    .flotantes span:nth-child(2) {left: 22%; animation-duration: 21s; animation-delay: 4s;  font-size: 2rem;}
    .flotantes span:nth-child(3) {left: 41%; animation-duration: 18s; animation-delay: 8s;}
    .flotantes span:nth-child(4) {left: 63%; animation-duration: 23s; animation-delay: 2s;  font-size: 3.2rem;}
    .flotantes span:nth-child(5) {left: 80%; animation-duration: 19s; animation-delay: 6s;  font-size: 2.2rem;}
    .flotantes span:nth-child(6) {left: 92%; animation-duration: 25s; animation-delay: 10s;}
    @keyframes sube {
        0%   {transform: translateY(0) rotate(-12deg); opacity: 0;}
        10%  {opacity: .22;}
        90%  {opacity: .22;}
        100% {transform: translateY(-115vh) rotate(18deg); opacity: 0;}}

    /* ================= TEXTO LEGIBLE ================= */
    .stApp, .stApp p, .stApp label, .stApp span, .stApp li {color: #F2F2F2;}
    .stApp h1, .stApp h2, .stApp h3 {color: #FFFFFF; font-weight: 800;}
    .stApp strong {color: #FFFFFF;}
    [data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] * {color: #b9cfc0 !important;}
    [data-testid="stToolbar"] *, [data-testid="stHeader"] * {color: #FFFFFF !important;}

    @keyframes flota {0%,100% {transform: translateY(0) rotate(-6deg);} 50% {transform: translateY(-12px) rotate(6deg);}}
    @keyframes brilla {0% {background-position: 0% 50%;} 100% {background-position: 200% 50%;}}
    @keyframes pulso {0%,100% {box-shadow: 0 0 0 0 rgba(0,230,118,.45);} 50% {box-shadow: 0 0 0 14px rgba(0,230,118,0);}}

    /* ================= HERO ================= */
    .hero {position: relative; overflow: hidden; color: #fff; border-radius: 28px; padding: 2.6rem 2.8rem;
           background: radial-gradient(circle at 85% 20%, rgba(0,230,118,.30), transparent 45%),
                       linear-gradient(120deg, rgba(2,10,5,.88), rgba(6,33,15,.88), rgba(11,59,28,.88), rgba(6,33,15,.88), rgba(2,10,5,.88));
           background-size: 100% 100%, 250% 100%; animation: brilla 10s linear infinite;
           border: 1px solid rgba(0,230,118,.4); box-shadow: 0 0 44px rgba(0,230,118,.22);
           backdrop-filter: blur(6px);}
    .hero h1 {color: #fff; font-weight: 800; font-size: 2.9rem; line-height: 1.1; margin: 0; padding: 0;
              text-shadow: 0 0 22px rgba(0,230,118,.5);}
    .hero p {font-size: 1.1rem; color: #d6f2df; margin: .8rem 0 0 0; max-width: 680px;}
    .hero .bill {position: absolute; right: 2.5rem; top: 1.2rem; font-size: 5.8rem; animation: flota 4s ease-in-out infinite;
                 filter: drop-shadow(0 0 18px rgba(0,230,118,.65));}
    .chip {display: inline-block; background: rgba(0,230,118,.12); border: 1px solid rgba(0,230,118,.5);
           color: #8dffbc; border-radius: 999px; padding: .25rem 1rem; margin: 1.1rem .45rem 0 0; font-size: .85rem;}

    /* ================= DENOMINACIONES ================= */
    .pill {display: inline-block; border-radius: 12px; padding: .5rem 1.1rem; margin: .3rem .4rem .3rem 0;
           font-weight: 800; font-size: 1.05rem;}
    .pill.on {background: linear-gradient(135deg, #00C853, #00E676); color: #00160a !important;
              box-shadow: 0 0 16px rgba(0,230,118,.5);}
    .pill.off {background: #121212; color: #6b6b6b !important; text-decoration: line-through; border: 1px solid #2a2a2a;}

    /* ================= TARJETAS ================= */
    .card {background: linear-gradient(160deg, rgba(15,15,15,.92), rgba(10,26,16,.92)); border: 1px solid #1f4a30;
           border-radius: 20px; padding: 1.3rem 1.4rem; height: 100%; backdrop-filter: blur(6px);
           transition: transform .2s, box-shadow .2s, border-color .2s;}
    .card:hover {transform: translateY(-5px); border-color: #00E676; box-shadow: 0 0 26px rgba(0,230,118,.28);}
    .card .ico {font-size: 2.1rem;}
    .card h4 {margin: .5rem 0 .3rem 0; color: #00E676; font-weight: 800;}
    .card p {margin: 0; font-size: .93rem; color: #dbe7df;}

    /* ================= RESULTADO ================= */
    .res {border-radius: 24px; padding: 1.6rem 1.8rem; color: #fff; margin-bottom: .8rem;}
    .res.ok {background: linear-gradient(135deg, #04210f, #0a5c2b 60%, #00C853);
             border: 1px solid #00E676; animation: pulso 2.4s infinite; box-shadow: 0 0 34px rgba(0,230,118,.38);}
    .res.no {background: linear-gradient(135deg, #1f1200, #6b3d00 60%, #E39A1B);
             border: 1px solid #ffb74d; box-shadow: 0 0 30px rgba(255,167,38,.3);}
    .res .sub {font-size: .95rem; color: #fff; opacity: .94; letter-spacing: .5px;}
    .res .big {font-size: 3.4rem; font-weight: 800; line-height: 1.1; color: #fff; text-shadow: 0 0 20px rgba(255,255,255,.3);}
    .res .conf {font-size: 1.05rem; margin-top: .3rem; color: #fff;}

    /* ================= COMPONENTES STREAMLIT ================= */
    [data-testid="stMetric"] {background: rgba(13,13,13,.9); border: 1px solid #1f4a30; border-radius: 16px; padding: .9rem 1.1rem;}
    [data-testid="stMetricLabel"], [data-testid="stMetricLabel"] * {color: #cfe0d5 !important;}
    [data-testid="stMetricValue"], [data-testid="stMetricValue"] * {color: #00E676 !important;}

    .stTabs [data-baseweb="tab-list"] {gap: .4rem; border-bottom: 1px solid #1f4a30;}
    .stTabs [data-baseweb="tab"] {font-weight: 600; font-size: 1rem;}
    .stTabs [data-baseweb="tab"] p {color: #b9cfc0 !important;}
    .stTabs [aria-selected="true"] p {color: #00E676 !important;}
    .stTabs [data-baseweb="tab-highlight"] {background-color: #00E676 !important;}

    /* Cargador de archivos */
    [data-testid="stFileUploaderDropzone"] {background: rgba(13,13,13,.92); border: 2px dashed #25a35a; border-radius: 16px;}
    [data-testid="stFileUploaderDropzone"], [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] small, [data-testid="stFileUploaderDropzone"] div {color: #e6f3ea !important;}
    [data-testid="stFileUploaderDropzone"] button, [data-testid="stFileUploaderDropzone"] button * {
        background: #00E676 !important; color: #00160a !important; font-weight: 700; border: none !important; border-radius: 10px;}
    [data-testid="stFileUploaderFile"], [data-testid="stFileUploaderFile"] * {color: #fff !important;}

    /* Camara */
    [data-testid="stCameraInput"] {background: rgba(13,13,13,.92); border: 1px solid #1f4a30; border-radius: 16px; padding: .6rem;}
    [data-testid="stCameraInput"] button, [data-testid="stCameraInput"] button * {
        background: #00E676 !important; color: #00160a !important; font-weight: 700; border-radius: 10px; border: none !important;}

    /* Lista desplegable de ejemplos */
    div[data-baseweb="select"] > div {background: #0d0d0d !important; border: 1px solid #25a35a !important; border-radius: 12px;}
    div[data-baseweb="select"] *, div[data-baseweb="select"] svg {color: #ffffff !important; fill: #ffffff !important;}
    div[data-baseweb="popover"], div[data-baseweb="popover"] ul, div[data-baseweb="menu"] {background: #0d0d0d !important;}
    div[data-baseweb="popover"] li, div[data-baseweb="popover"] li * {color: #ffffff !important; background: #0d0d0d !important;}
    div[data-baseweb="popover"] li:hover, div[data-baseweb="popover"] li[aria-selected="true"] {background: #0e3a20 !important;}

    [data-testid="stRadio"] label p {color: #ffffff !important; font-weight: 600;}
    [data-testid="stExpander"] {background: rgba(13,13,13,.9); border: 1px solid #1f4a30; border-radius: 14px;}
    [data-testid="stExpander"] summary, [data-testid="stExpander"] summary * {color: #ffffff !important;}
    [data-testid="stAlert"] {background: rgba(13,26,18,.92); border: 1px solid #1f4a30; border-radius: 14px;}
    [data-testid="stAlert"] * {color: #e6f3ea !important;}
    .stProgress > div > div > div > div {background: linear-gradient(90deg, #00C853, #00E676);}
    .pie {text-align: center; color: #86b99a; font-size: .85rem; margin-top: 2.2rem;}

    /* Boton de subir archivo: solo dice "Cargar" */
    [data-testid="stFileUploaderDropzone"] button {position: relative; font-size: 0 !important; min-width: 130px; min-height: 42px;}
    [data-testid="stFileUploaderDropzone"] button * {display: none !important;}
    [data-testid="stFileUploaderDropzone"] button::after {content: "Cargar"; display: block; font-size: 1rem;
        font-weight: 800; color: #00160a; font-family: 'Poppins', sans-serif;}

    /* Texto de ayuda en español */
    [data-testid="stFileUploaderDropzone"] small {font-size: 0 !important;}
    [data-testid="stFileUploaderDropzone"] small::after {content: "Máximo 10 MB por archivo • JPG, PNG, BMP, WEBP";
        font-size: .85rem; color: #cfe0d5; font-family: 'Poppins', sans-serif;}

    /* Evita que los iconos de Streamlit se vean como texto */
    [data-testid="stIconMaterial"], .material-symbols-rounded {font-family: 'Material Symbols Rounded' !important;}
    </style>

    <div class="flotantes" translate="no"><span>💵</span><span>💰</span><span>💵</span><span>💸</span><span>💵</span><span>💰</span></div>

    <div class="hero">
      <div class="bill">💵</div>
      <h1>Reconocedor de<br>billetes mexicanos</h1>
      <p>Sube una foto o usa tu cámara y descubre al instante cuántos <b>pesos</b> vale el billete,
         con su nivel de confianza y el análisis completo.</p>
      <span class="chip">Visión por computadora</span><span class="chip">OpenCV</span>
      <span class="chip">Histograma HSV</span><span class="chip">ORB + RANSAC</span>
    </div>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource(show_spinner=False)
def obtener_plantillas():
    """Carga las plantillas una sola vez y las conserva en memoria."""
    return billetes.cargar_plantillas()


def leer_imagen(archivo):
    """Decodifica la imagen subida validando tamano y contenido. Devuelve None si no es valida."""
    contenido = archivo.getvalue()
    if len(contenido) > cfg.MAX_UPLOAD_MB * 1024 * 1024:
        st.error("La imagen supera el máximo de %d MB." % cfg.MAX_UPLOAD_MB)
        return None
    img = cv2.imdecode(np.frombuffer(contenido, dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        st.error("El archivo no es una imagen válida o está dañado.")
    return img


def bgr_a_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def mostrar_imagen(img, **kwargs):
    """st.image compatible con versiones nuevas (width) y anteriores (use_container_width)."""
    try:
        st.image(img, width="stretch", **kwargs)
    except TypeError:
        st.image(img, use_container_width=True, **kwargs)


plantillas = obtener_plantillas()
activas = sorted({p["den"] for p in plantillas}) if plantillas else []

st.write("")
tab_probar, tab_como, tab_acerca = st.tabs(["🔍 Probar", "⚙️ Cómo funciona", "ℹ️ Acerca del proyecto"])

# ------------------------------------------------------------------ PROBAR
with tab_probar:
    pills = "".join('<span class="pill %s" translate="no">%d pesos</span>' % ("on" if d in activas else "off", d)
                    for d in billetes.DENOMINACIONES)
    st.markdown("**Denominaciones disponibles (pesos mexicanos):** " + pills, unsafe_allow_html=True)

    if not plantillas:
        st.error("No hay plantillas disponibles. Agrega imágenes en plantillas/20, plantillas/50, etc.")
        st.stop()

    opciones = ["📁 Subir fotografía", "📷 Usar cámara"] + (["🖼️ Imagen de ejemplo"] if EJEMPLOS else [])
    fuente = st.radio("¿Cómo quieres probarlo?", opciones, horizontal=True)

    img = None
    if fuente.startswith("📁"):
        archivo = st.file_uploader("Selecciona la fotografía de un billete",
                                   type=["jpg", "jpeg", "png", "bmp", "webp"])
        if archivo is not None:
            img = leer_imagen(archivo)
    elif fuente.startswith("📷"):
        archivo = st.camera_input("Toma una fotografía del billete")
        if archivo is not None:
            img = leer_imagen(archivo)
    else:
        nombre = st.selectbox("Elige un ejemplo", [p.name for p in EJEMPLOS])
        img = cv2.imread(str(BASE_DIR / "ejemplos" / nombre))

    if img is None:
        st.markdown(
            '<div class="card"><div class="ico">💡</div><h4>Consejos para un buen resultado</h4>'
            "<p>Usa buena luz, muestra el billete completo, colócalo sobre un fondo liso "
            "y mantén la cámara enfocada.</p></div>", unsafe_allow_html=True)
    else:
        with st.spinner("Analizando billete..."):
            recorte, caja, valido = billetes.segmentar(img)
            denominacion, confianza, detalle = billetes.clasificar(recorte, plantillas)

        anotada = billetes.anotar(img, caja if valido else None, billetes.etiqueta(denominacion, confianza),
                                  (0, 200, 0) if denominacion is not None else (0, 0, 255))
        izq, der = st.columns([1.1, 1])
        with izq:
            st.subheader("Imagen analizada")
            mostrar_imagen(bgr_a_rgb(anotada))
        with der:
            if denominacion is not None:
                st.markdown('<div class="res ok" translate="no"><div class="sub">✅ BILLETE IDENTIFICADO · PESOS MEXICANOS (MXN)</div>'
                            '<div class="big">%d pesos</div><div class="conf">Confianza %.1f%%</div></div>'
                            % (denominacion, confianza * 100), unsafe_allow_html=True)
            else:
                st.markdown('<div class="res no"><div class="sub">⚠️ No se pudo identificar con suficiente confianza</div>'
                            '<div class="big">No reconocido</div><div class="conf">Mejor puntaje %.1f%%</div></div>'
                            % (confianza * 100), unsafe_allow_html=True)
            st.progress(float(min(max(confianza, 0.0), 1.0)))
            c1, c2 = st.columns(2)
            c1.metric("Segmentación", "Detectado" if valido else "Imagen completa")
            c2.metric("Umbral de aceptación", "%d%%" % round(billetes.UMBRAL_ACEPTACION * 100))
            st.markdown("**Puntaje por denominación (pesos)**")
            st.bar_chart({"%d pesos" % d: round(s, 3) for d, s in sorted(detalle.items())}, y_label="Puntaje")
        with st.expander("Ver imagen rectificada (600 × 280 px)"):
            mostrar_imagen(bgr_a_rgb(recorte), caption="Recorte normalizado que recibe el clasificador")

# ------------------------------------------------------------ COMO FUNCIONA
with tab_como:
    st.subheader("Del fotograma a la denominación en 5 pasos")
    pasos = [("✂️", "1. Segmentación", "Detecta los bordes y localiza el contorno principal del billete."),
             ("📐", "2. Perspectiva", "Endereza el billete y lo normaliza a 600 × 280 píxeles."),
             ("🎨", "3. Color", "Calcula un histograma HSV y lo compara con cada plantilla."),
             ("🔎", "4. Detalles", "Busca puntos ORB y valida las coincidencias con RANSAC."),
             ("🏆", "5. Decisión", "Combina 35 % color y 65 % ORB. Bajo 0.35 no lo acepta.")]
    for col, (ico, titulo, texto) in zip(st.columns(5), pasos):
        col.markdown('<div class="card"><div class="ico">%s</div><h4>%s</h4><p>%s</p></div>' % (ico, titulo, texto),
                     unsafe_allow_html=True)
    st.write("")
    st.info("Si el parecido con todas las plantillas es bajo, la aplicación responde *No reconocido* "
            "en lugar de adivinar.")

# ------------------------------------------------------------------- ACERCA
with tab_acerca:
    izq, der = st.columns(2)
    with izq:
        st.subheader("Proyecto")
        st.markdown("Aplicación de visión por computadora que identifica billetes mexicanos (pesos) usando **Python, OpenCV "
                    "y Streamlit**.\n\n"
                    "**Universidad Autónoma del Estado de México**  \nCentro Universitario UAEM Nezahualcóyotl  \n"
                    "Ingeniería en Sistemas Inteligentes · Semestre noveno%s" % (" · Grupo %s" % GRUPO if GRUPO else ""))
    with der:
        st.subheader("Equipo")
        st.markdown("\n".join("- %s" % n for n in EQUIPO) + "\n\n**Profesor:** Víctor Antonio Flores Lezama")
    st.subheader("Limitaciones")
    st.markdown("- Solo reconoce las denominaciones con plantilla registrada (activas arriba).\n"
                "- Funciona mejor con buena luz y fondo liso.\n"
                "- No se ha medido la exactitud con un conjunto amplio de fotografías reales.")

st.markdown('<div class="pie">Hecho con OpenCV y Streamlit · UAEM CU Nezahualcóyotl</div>', unsafe_allow_html=True)
