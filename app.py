"""
Proyecto: Sistema de IA Disruptiva y Multi-Agente
Autor: Joonathan Cardozo
Descripción: Aplicación web interactiva en Streamlit que simula una red de 
nodos de IA colaborativos usando Gemini para resolución de problemas complejos.
"""

from google import genai
from google.genai import errors
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="IA Disruptiva - Red Multi-Agente", page_icon="⚡", layout="wide"
)

# --- Título y Descripción ---
st.title("⚡ Red de IA Disruptiva y Multi-Agente")
st.caption(
    "Arquitectura distribuida y colaborativa para procesamiento avanzado con"
    " Gemini."
)

# --- Configuración de la API Key en la barra lateral con Memoria ---
st.sidebar.header("⚙️ Configuración del Nodo")

if "api_key" not in st.session_state:
  st.session_state.api_key = ""

api_key_input = st.sidebar.text_input(
    "🔑 API Key de Gemini:",
    value=st.session_state.api_key,
    type="password",
    placeholder="Pega aquí tu clave...",
)

if api_key_input:
  st.session_state.api_key = api_key_input

api_key = st.session_state.api_key

if api_key:
  try:
    client = genai.Client(api_key=api_key)
  except Exception as e:
    st.error(f"Error al inicializar el cliente: {e}")
    st.stop()
else:
  st.info("👈 Ingresa tu API Key en la barra lateral para activar la red.")
  st.stop()

# --- Panel Principal de Tareas ---
st.subheader("📥 Inserción de Objetivo Disruptivo")
objetivo = st.text_area(
    "Describe el reto o proyecto que la red multi-agente debe resolver:",
    placeholder=(
        "Ej: Crear una startup de tecnología verde impulsada por inteligencia"
        " artificial."
    ),
)

if st.button("🚀 Ejecutar Pipeline Multi-Agente", type="primary"):
  if objetivo:
    st.markdown("---")
    st.markdown("### 🔄 Procesamiento Distribuido en Red")

    # --- NODO 1: EL ESTRATEGA ---
    with st.status(
        "🧠 Nodo 1: Agente Estratega analizando el mercado...", expanded=True
    ) as status_1:
      prompt_1 = f"Actúa como un Consultor Estratégico Global. Analiza disruptivamente el siguiente objetivo y plantea los pilares fundamentales: {objetivo}"
      try:
        resp_1 = client.models.generate_content(
            model="gemini-3.8-flash", contents=prompt_1
        )
        texto_1 = resp_1.text
        status_1.update(
            label="Nodo 1: Estratega (Completado)",
            state="complete",
            expanded=False,
        )
      except errors.APIError as e:
        st.error(f"Error en Nodo 1: {e}")
        st.stop()

    with st.expander("📄 Ver Análisis del Nodo 1 (Estratega)"):
      st.write(texto_1)

    # --- NODO 2: EL INNOVADOR TÉCNICO ---
    with st.status(
        "💻 Nodo 2: Agente Tecnológico diseñando la solución...", expanded=True
    ) as status_2:
      prompt_2 = f"Tomando como base la estrategia anterior, diseña la propuesta técnica detallada o arquitectura de software necesaria:\n\n{texto_1}"
      try:
        resp_2 = client.models.generate_content(
            model="gemini-3.8-flash", contents=prompt_2
        )
        texto_2 = resp_2.text
        status_2.update(
            label="Nodo 2: Tecnológico (Completado)",
            state="complete",
            expanded=False,
        )
      except errors.APIError as e:
        st.error(f"Error en Nodo 2: {e}")
        st.stop()

    with st.expander("🛠️ Ver Propuesta del Nodo 2 (Tecnológico)"):
      st.markdown(texto_2)

    # --- NODO 3: EL AUDITOR DE RIESGOS ---
    with st.status(
        "🛡️ Nodo 3: Agente Auditor evaluando viabilidad y seguridad...",
        expanded=True,
    ) as status_3:
      prompt_3 = f"Actúa como un Auditor de Riesgos y Viabilidad. Evalúa críticamente la siguiente propuesta técnica, detecta fallos potenciales y entrega un veredicto de optimización:\n\n{texto_2}"
      try:
        resp_3 = client.models.generate_content(
            model="gemini-3.8-flash", contents=prompt_3
        )
        texto_3 = resp_3.text
        status_3.update(
            label="Nodo 3: Auditor (Completado)",
            state="complete",
            expanded=False,
        )
      except errors.APIError as e:
        st.error(f"Error en Nodo 3: {e}")
        st.stop()

    # --- RESULTADO FINAL CONSOLIDADO ---
    st.markdown("---")
    st.subheader("🎯 Resultado Consolidado de la Red Disruptiva")
    st.success(
        "¡El sistema multi-agente ha completado el procesamiento colaborativo!"
    )
    st.markdown(texto_3)

  else:
    st.warning("Por favor ingresa un reto para que la red comience a trabajar.")