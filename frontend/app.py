import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
import plotly.express as px
import folium
from streamlit_folium import st_folium
import os
import sys

# Add root folder to python path for direct imports (Embedded Fallback Mode)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from backend.app.models import predict_bearing_fault
    from ai.agents import explain_maintenance_fault
except ImportError:
    predict_bearing_fault = None
    explain_maintenance_fault = None

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(
    page_title="MineAssist-PdM",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Sleek CSS Styles for Dark-themed Premium Aesthetics
st.markdown("""
<style>
    .main {
        background-color: #0f111a;
        color: #ffffff;
    }
    div[data-testid="stMetric"] {
        background-color: #1a1c28;
        border: 1px solid #2d3142;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    div[data-testid="stSidebar"] {
        background-color: #0b0c10;
        border-right: 1px solid #1f2833;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1a1c28;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        border: 1px solid #2d3142;
        color: #c5c6c7;
    }
    .stTabs [aria-selected="true"] {
        background-color: #45f3ff;
        color: #0f111a !important;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #45f3ff;
        color: #0f111a;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #66fcf1;
        box-shadow: 0px 0px 10px #66fcf1;
    }
    .status-ok {
        color: #00ff88;
        font-weight: bold;
    }
    .status-warning {
        color: #ffaa00;
        font-weight: bold;
    }
    .status-danger {
        color: #ff3333;
        font-weight: bold;
    }
</style>
""", unsafe_type_encoding=True)

# Helper: Check API Status
@st.cache_data(ttl=10)
def check_backend_status():
    try:
        response = requests.get(BACKEND_URL, timeout=1.5)
        if response.status_code == 200:
            return True, response.json().get("service", "API Activa")
    except Exception:
        pass
    return False, "Modo Embebido (Backend sin conexión)"

api_online, api_status = check_backend_status()

# Load local dataset for demo assets
@st.cache_data
def load_assets_telemetry():
    # If API is online, fetch from backend. Otherwise, load local CSV directly.
    if api_online:
        try:
            response = requests.get(f"{BACKEND_URL}/assets", timeout=2)
            if response.status_code == 200:
                return pd.DataFrame(response.json())
        except Exception:
            pass
            
    # Local fallback
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/machine_telemetry.csv"))
    if os.path.exists(path):
        return pd.read_csv(path)
    
    # Minimal static dataframe if file missing
    return pd.DataFrame([
        {"machine_id": "M001", "name": "Molino de Bolas 01", "latitude": -14.0985, "longitude": -72.3220, "rms": 0.082, "kurtosis": 2.84, "crest_factor": 3.21, "temperature": 38.2, "speed": 1797, "status": "Normal"},
        {"machine_id": "M003", "name": "Bomba de Relaves P-03", "latitude": -14.0975, "longitude": -72.3210, "rms": 0.320, "kurtosis": 7.12, "crest_factor": 6.45, "temperature": 48.4, "speed": 1750, "status": "Critico (Falla Rodamiento)"}
    ])

assets_df = load_assets_telemetry()

# Sidebar Setup
with st.sidebar:
    st.image("https://miro.medium.com/v2/resize:fit:320/0*cgCaGtJhYVbUvMrb.png", width=100) # Optional placeholder logo
    st.title("MineAssist-PdM")
    st.markdown("---")
    st.markdown(f"**Estado de API:**")
    if api_online:
        st.markdown(f"<span class='status-ok'>● Conectado a la API ({api_status})</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span class='status-warning'>● Offline: {api_status}</span>", unsafe_allow_html=True)
        st.info("Usando lógica interna e inferencia local en memoria.")
        
    st.markdown("---")
    st.markdown("### 🏢 Unidad Minera:")
    st.markdown("**Minera Las Bambas** (Apurímac, Perú)")
    st.markdown("---")
    st.markdown("### 🏷️ Repositorio & Autor:")
    st.markdown("- **Founder:** John Barraza")
    st.markdown("- **UP ID:** BARRAZA RATACHI, John Svante")
    st.markdown("- **Licencia:** MIT")

st.title("⚙️ Copiloto de Mantenimiento Predictivo Minero")
st.markdown("##### Monitoreo de vibraciones de fajas, molinos y bombas de relaves georreferenciados mediante Inteligencia Artificial y Machine Learning.")

# Setup Tabs
tab_general, tab_predictive, tab_copilot, tab_ingest = st.tabs([
    "📊 Panel General y GIS", 
    "📈 Análisis Predictivo (Rodamientos)", 
    "💬 Asistente IA (Explicabilidad)", 
    "📝 Ingesta de Manuales y Voz (OCR/Whisper)"
])

# --- TAB 1: Panel General y GIS ---
with tab_general:
    st.header("📍 Mapeo de Activos Críticos y Criticidad en Las Bambas")
    st.markdown("A continuación se geolocalizan los equipos de la planta de beneficio. El color indica el nivel de criticidad según el modelo predictivo.")
    
    # Metrics Row
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    total_assets = len(assets_df)
    critical_assets = len(assets_df[assets_df["status"].str.contains("Critico|Falla", case=False)])
    warning_assets = len(assets_df[assets_df["status"].str.contains("Aviso|Alerta", case=False)])
    normal_assets = total_assets - critical_assets - warning_assets
    
    with m_col1:
        st.metric("Total Activos Monitoreados", total_assets)
    with m_col2:
        st.metric("Condición Normal", normal_assets, delta=f"{normal_assets} estables", delta_color="normal")
    with m_col3:
        st.metric("Condición en Alerta", warning_assets, delta=f"{warning_assets} corregir", delta_color="inverse")
    with m_col4:
        st.metric("Condición Crítica", critical_assets, delta=f"{critical_assets} paradas inminentes", delta_color="inverse")
        
    # Map & Table Layout
    map_col, table_col = st.columns([2, 1])
    
    with map_col:
        # Create Folium Map centered on Las Bambas
        m = folium.Map(location=[-14.0985, -72.3220], zoom_start=16, tiles="CartoDB dark_matter")
        
        for idx, row in assets_df.iterrows():
            status_lower = str(row["status"]).lower()
            if "critico" in status_lower:
                color = "red"
            elif "aviso" in status_lower or "alerta" in status_lower:
                color = "orange"
            else:
                color = "green"
                
            popup_html = f"""
            <div style="color: black; font-family: sans-serif; width: 180px;">
                <b>{row['name']}</b><br/>
                ID: {row['machine_id']}<br/>
                RMS: {row['rms']} g<br/>
                Temperatura: {row['temperature']} °C<br/>
                <b>Estado: {row['status']}</b>
            </div>
            """
            
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=folium.Popup(popup_html, max_width=250),
                tooltip=row["name"],
                icon=folium.Icon(color=color, icon="cog", prefix="fa")
            ).add_to(m)
            
        st_folium(m, width="100%", height=450, returned_objects=[])
        
    with table_col:
        st.markdown("### 📋 Resumen de Telemetría")
        st.dataframe(
            assets_df[["machine_id", "name", "rms", "temperature", "status"]],
            use_container_width=True,
            hide_index=True
        )

# --- TAB 2: Análisis Predictivo (Rodamientos) ---
with tab_predictive:
    st.header("📈 Simulación e Inferencia de Fallas en Rodamientos (Dataset CWRU)")
    st.markdown("Selecciona un activo o ajusta manualmente los valores para probar el modelo de Machine Learning (XGBoost/Random Forest entrenado con el dataset de CWRU).")
    
    # Select asset for preset values
    selected_name = st.selectbox("Cargar preajuste de un activo:", assets_df["name"].tolist())
    preset = assets_df[assets_df["name"] == selected_name].iloc[0]
    
    # Input Sliders layout
    col_in1, col_in2 = st.columns(2)
    
    with col_in1:
        rms_val = st.slider("Valor RMS de Vibración (g)", 0.04, 0.50, float(preset["rms"]), step=0.005)
        kurtosis_val = st.slider("Factor de Curtosis", 2.0, 10.0, float(preset["kurtosis"]), step=0.1)
        crest_factor_val = st.slider("Factor de Cresta", 2.0, 8.0, float(preset["crest_factor"]), step=0.05)
        
    with col_in2:
        skewness_val = st.slider("Asimetría (Skewness)", -1.0, 1.5, -0.1 if selected_name == "Molino de Bolas 01" else 0.5, step=0.05)
        temp_val = st.slider("Temperatura del Rodamiento (°C)", 30.0, 95.0, float(preset["temperature"]), step=0.5)
        speed_val = st.slider("Velocidad de Operación (RPM)", 1700, 1800, int(preset["speed"]), step=1)

    # Inferencia
    telemetry_input = {
        "rms": rms_val,
        "kurtosis": kurtosis_val,
        "crest_factor": crest_factor_val,
        "skewness": skewness_val,
        "temperature": temp_val,
        "speed": speed_val
    }
    
    if api_online:
        try:
            response = requests.post(f"{BACKEND_URL}/predict", json=telemetry_input)
            if response.status_code == 200:
                pred_result = response.json()
            else:
                pred_result = {"error": response.text}
        except Exception as e:
            pred_result = {"error": str(e)}
    else:
        # Embedded local fallback
        if predict_bearing_fault:
            pred_result = predict_bearing_fault(
                rms=rms_val,
                kurtosis=kurtosis_val,
                crest_factor=crest_factor_val,
                skewness=skewness_val,
                temperature=temp_val,
                speed=speed_val
            )
        else:
            # Absolute mock if imports fail
            pred_result = {
                "prediction": "Normal" if rms_val < 0.12 else "Outer_Race" if kurtosis_val > 6 else "Inner_Race",
                "severity": "Bajo" if rms_val < 0.12 else "Crítico" if kurtosis_val > 6 else "Aviso",
                "probabilities": {"Normal": 0.9, "Inner_Race": 0.05, "Outer_Race": 0.03, "Ball": 0.02}
            }

    # Display prediction results
    st.markdown("---")
    res_col1, res_col2 = st.columns([1, 1])
    
    with res_col1:
        st.markdown("### 🎯 Resultado del Diagnóstico")
        pred_label = pred_result.get("prediction", "Normal")
        severity_label = pred_result.get("severity", "Bajo")
        
        # Color matching
        col_span = "status-ok" if pred_label == "Normal" else "status-danger" if severity_label == "Crítico" else "status-warning"
        
        st.markdown(f"**Clasificación Detectada:** <span class='{col_span}' style='font-size:24px;'>{pred_label}</span>", unsafe_allow_html=True)
        st.markdown(f"**Severidad de la Falla:** <span class='{col_span}' style='font-size:20px;'>{severity_label}</span>", unsafe_allow_html=True)
        
        # Simulated live vibration signal plot
        st.markdown("#### 📉 Simulación de Onda de Tiempo de Aceleración")
        t = [i * 0.001 for i in range(200)]
        # Generate wave based on selected fault type
        if pred_label == "Normal":
            wave = [0.08 * (pd.np.sin(2 * pd.np.pi * 30 * x) + 0.3 * pd.np.random.randn()) for x in t] if hasattr(pd, "np") else [0.08 * (3.14 * x) for x in t] # minimal fallback
        else:
            # Impact pulses
            wave = [rms_val * (0.6 * pd.np.sin(2 * pd.np.pi * 30 * x) + (2.0 if (i % 25 == 0) else 0.1) * pd.np.random.randn()) for i, x in enumerate(t)] if hasattr(pd, "np") else [0.2 * x for x in t]
            
        fig_wave = go.Figure()
        fig_wave.add_trace(go.Scatter(x=t, y=wave, mode='lines', name='Vibración (g)', line=dict(color='#45f3ff')))
        fig_wave.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="white"),
            margin=dict(l=20, r=20, t=20, b=20),
            height=200
        )
        st.plotly_chart(fig_wave, use_container_width=True)

    with res_col2:
        st.markdown("### 📊 Distribución de Probabilidades")
        probs = pred_result.get("probabilities", {"Normal": 1.0, "Inner_Race": 0.0, "Outer_Race": 0.0, "Ball": 0.0})
        
        fig_probs = px.bar(
            x=list(probs.keys()),
            y=list(probs.values()),
            labels={'x': 'Condición', 'y': 'Probabilidad'},
            color_discrete_sequence=['#66fcf1']
        )
        fig_probs.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="white"),
            margin=dict(l=20, r=20, t=20, b=20),
            height=280
        )
        st.plotly_chart(fig_probs, use_container_width=True)

    # Save details in session state for AI chatbot tab
    st.session_state["last_prediction"] = pred_result
    st.session_state["last_telemetry"] = telemetry_input
    st.session_state["last_machine_name"] = selected_name

# --- TAB 3: Asistente IA (Explicabilidad) ---
with tab_copilot:
    st.header("💬 Copiloto de IA: Explicación de Falla y Plan de Acción")
    st.markdown("Este módulo traduce la telemetría y el diagnóstico matemático del modelo de Machine Learning a recomendaciones estructuradas en lenguaje natural.")
    
    # Check if a prediction is available in session state
    if "last_prediction" not in st.session_state:
        st.warning("Primero ve a la pestaña 'Análisis Predictivo' e inicia una predicción para cargar los datos del sensor.")
    else:
        st.markdown(f"**Activo seleccionado:** `{st.session_state['last_machine_name']}`")
        st.markdown(f"**Resultado de Clasificación:** `{st.session_state['last_prediction'].get('prediction')}`")
        
        if st.button("Generar Reporte de Mantenimiento Asistido por IA"):
            with st.spinner("Invocando al agente de mantenimiento de IA..."):
                explain_data = {
                    "machine_name": st.session_state["last_machine_name"],
                    "telemetry": st.session_state["last_telemetry"],
                    "prediction_result": st.session_state["last_prediction"]
                }
                
                if api_online:
                    try:
                        response = requests.post(f"{BACKEND_URL}/explain", json=explain_data)
                        if response.status_code == 200:
                            ai_explanation = response.json().get("explanation")
                        else:
                            ai_explanation = f"Error en API de Agente: {response.text}"
                    except Exception as e:
                        ai_explanation = f"Error al conectar con el Agente: {str(e)}"
                else:
                    if explain_maintenance_fault:
                        ai_explanation = explain_maintenance_fault(
                            machine_name=st.session_state["last_machine_name"],
                            telemetry=st.session_state["last_telemetry"],
                            prediction_result=st.session_state["last_prediction"]
                        )
                    else:
                        ai_explanation = "La lógica de IA no está disponible localmente."
                        
            st.markdown("### 📋 Reporte Técnico de Mantenimiento")
            st.markdown(ai_explanation)

# --- TAB 4: Ingesta de Manuales y Voz (OCR/Whisper) ---
with tab_ingest:
    st.header("📝 Módulos Auxiliares: Extracción Documental (OCR) y Transcripción (Whisper)")
    st.markdown("En esta sección se integran y justifican las herramientas del stack del curso para ingresar datos al sistema.")
    
    ocr_col, voice_col = st.columns(2)
    
    with ocr_col:
        st.markdown("### 📖 Ingesta de Ficha Técnica / Manual (PaddleOCR)")
        st.markdown("Sube el PDF del manual de tu motor/rodamiento para extraer frecuencias de falla características y cargarlas al sistema de alertas.")
        
        pdf_file = st.file_uploader("Subir manual de rodamiento (PDF)", type=["pdf"])
        manual_text = st.text_area("O pega fragmentos del manual técnico aquí:", placeholder="Ej. SKF 6312: Max RPM 5000, BPFI 148.5 Hz, BPFO 91.5 Hz...")
        
        if st.button("Procesar Manual Técnico"):
            if not pdf_file and not manual_text:
                st.error("Sube un archivo PDF o pega texto para procesar.")
            else:
                with st.spinner("Procesando documento mediante OCR y LLM..."):
                    if api_online:
                        try:
                            # Send Form data
                            files = {"file": pdf_file} if pdf_file else None
                            data = {"manual_text": manual_text} if manual_text else {}
                            response = requests.post(f"{BACKEND_URL}/parse-manual", files=files, data=data)
                            if response.status_code == 200:
                                ocr_res = response.json().get("extracted_data")
                            else:
                                ocr_res = {"error": response.text}
                        except Exception as e:
                            ocr_res = {"error": str(e)}
                    else:
                        # Simulated local fallback
                        ocr_res = {
                            "documento_leido": pdf_file.name if pdf_file else "Texto manual",
                            "modelo_motor": "WEG W22 Premium 50 HP",
                            "modelo_rodamiento": "SKF 6312 2Z/C3",
                            "frecuencias_falla_calculadas": {
                                "BPFI (Pista Interna)": "148.5 Hz",
                                "BPFO (Pista Externa)": "91.5 Hz"
                            },
                            "temperatura_max_operacion": "85.0 °C",
                            "lubricante_recomendado": "Mobilith SHC 100"
                        }
                        
                st.success("¡Datos extraídos con éxito!")
                st.json(ocr_res)
                
    with voice_col:
        st.markdown("### 🎤 Bitácora por Notas de Voz (Whisper)")
        st.markdown("Permite a los mecánicos reportar hallazgos acústicos en el tajo o planta mediante audio (transcrito con Whisper) para registrar incidentes automáticamente.")
        
        audio_file = st.file_uploader("Subir reporte de audio (WAV, MP3, M4A)", type=["wav", "mp3", "m4a"])
        voice_text = st.text_input("O ingresa la transcripción de voz simulada:", value="Se escucha un traqueteo metálico extraño y alta vibración en la Bomba de Relaves P-03, la temperatura se siente alta al tacto.")
        
        if st.button("Registrar Incidente por Voz"):
            with st.spinner("Transcribiendo y analizando reporte acústico..."):
                if api_online:
                    try:
                        files = {"file": audio_file} if audio_file else None
                        data = {"transcript_text": voice_text}
                        response = requests.post(f"{BACKEND_URL}/voice-log", files=files, data=data)
                        if response.status_code == 200:
                            voice_res = response.json()
                        else:
                            voice_res = {"error": response.text}
                    except Exception as e:
                        voice_res = {"error": str(e)}
                else:
                    voice_res = {
                        "status": "success",
                        "transcription": voice_text,
                        "action_taken": "Incidente registrado automáticamente en bitácora digital (Simulado local)",
                        "severity": "Crítico" if "P-03" in voice_text or "alta" in voice_text else "Aviso"
                    }
                    
            st.success("¡Incidente logueado!")
            st.write(voice_res)
