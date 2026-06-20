import os
import pandas as pd
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.models import predict_bearing_fault
from ai.agents import explain_maintenance_fault

app = FastAPI(title="MineAssist-PdM API", version="1.0.0")

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))
TELEMETRY_PATH = os.path.join(DATA_DIR, "machine_telemetry.csv")

class PredictRequest(BaseModel):
    rms: float
    kurtosis: float
    crest_factor: float
    skewness: float
    temperature: float
    speed: float

class ExplainRequest(BaseModel):
    machine_name: str
    telemetry: Dict[str, float]
    prediction_result: Dict[str, Any]

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "MineAssist-PdM Backend API",
        "available_endpoints": [
            "GET /assets - Listar activos y telemetría",
            "POST /predict - Predecir fallas de rodamientos",
            "POST /explain - Explicación de fallas asistida por IA",
            "POST /parse-manual - Simulación de Extracción Documental (OCR/AI)",
            "POST /voice-log - Simulación de Transcripción de Reportes por Voz (Whisper)"
        ]
    }

@app.get("/assets")
def get_assets():
    if not os.path.exists(TELEMETRY_PATH):
        raise HTTPException(status_code=404, detail="No se encontró el archivo de telemetría de activos.")
    try:
        df = pd.read_csv(TELEMETRY_PATH)
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer datos de telemetría: {str(e)}")

@app.post("/predict")
def predict(request: PredictRequest):
    result = predict_bearing_fault(
        rms=request.rms,
        kurtosis=request.kurtosis,
        crest_factor=request.crest_factor,
        skewness=request.skewness,
        temperature=request.temperature,
        speed=request.speed
    )
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/explain")
def explain(request: ExplainRequest):
    try:
        explanation = explain_maintenance_fault(
            machine_name=request.machine_name,
            telemetry=request.telemetry,
            prediction_result=request.prediction_result
        )
        return {"explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar explicación por IA: {str(e)}")

@app.post("/parse-manual")
async def parse_manual(
    file: Optional[UploadFile] = File(None),
    manual_text: Optional[str] = Form(None)
):
    """
    Simulación de Document AI / PaddleOCR sobre manuales técnicos.
    Extrae especificaciones clave del rodamiento del motor.
    """
    filename = file.filename if file else "Texto ingresado"
    
    # Simulates extracting structural data from the manual
    extracted_specs = {
        "documento_leido": filename,
        "modelo_motor": "WEG W22 Premium 50 HP",
        "modelo_rodamiento": "SKF 6312 2Z/C3",
        "frecuencias_falla_calculadas": {
            "BPFI (Pista Interna)": "148.5 Hz",
            "BPFO (Pista Externa)": "91.5 Hz",
            "BSF (Bolas)": "58.2 Hz",
            "FTF (Canastilla)": "14.1 Hz"
        },
        "temperatura_max_operacion": "85.0 °C",
        "lubricante_recomendado": "Mobilith SHC 100",
        "intervalo_relubricacion": "3,500 horas"
    }
    
    return {
        "status": "success",
        "message": "Manual procesado exitosamente mediante OCR estructurado (simulado).",
        "extracted_data": extracted_specs
    }

@app.post("/voice-log")
async def voice_log(
    file: Optional[UploadFile] = File(None),
    transcript_text: Optional[str] = Form(None)
):
    """
    Simulación de Whisper transcripción de notas de voz de operadores.
    Registra observaciones auditivas e integra detección de criticidad.
    """
    # If audio is sent, we simulate transcribing it
    text_result = transcript_text or "Se registra ruido inusual de traqueteo metálico y alta vibración en la faja transportadora CV-02, sospecha de desalineación severa y falta de grasa."
    
    # Analyze text using simple rule-based keywords for logging
    detected_severity = "Aviso"
    if any(word in text_result.lower() for word in ["fuerte", "critico", "humo", "inmediato", "parar"]):
        detected_severity = "Crítico"
        
    return {
        "status": "success",
        "transcription": text_result,
        "action_taken": "Incidente registrado automáticamente en bitácora digital",
        "severity": detected_severity,
        "logged_at": "2026-06-19T18:00:00"
    }
