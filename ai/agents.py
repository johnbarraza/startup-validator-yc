import os
import openai
import google.generativeai as genai

# Explains bearing faults and outputs recommendations in Spanish
def explain_maintenance_fault(machine_name: str, telemetry: dict, prediction_result: dict) -> str:
    prediction = prediction_result.get("prediction", "Desconocido")
    severity = prediction_result.get("severity", "Desconocido")
    probabilities = prediction_result.get("probabilities", {})
    
    # Format telemetry data for prompt
    telemetry_str = ", ".join([f"{k}: {v}" for k, v in telemetry.items()])
    
    prompt = f"""
    Actúa como un Ingeniero Senior de Mantenimiento Predictivo en una unidad minera (Las Bambas, Perú).
    
    Se ha detectado una anomalía en el rodamiento del siguiente equipo:
    - Nombre del Equipo: {machine_name}
    - Lectura de Sensores: {telemetry_str}
    - Diagnóstico del Modelo de ML: {prediction} (Severidad: {severity})
    - Distribución de Probabilidades del Modelo: {probabilities}
    
    Escribe un reporte de explicación y plan de acción en español que contenga:
    1. **Explicación del Diagnóstico**: Explica en términos físicos sencillos qué significa tener una falla tipo '{prediction}' en un rodamiento y por qué los sensores (como el factor de cresta o curtosis) sustentan esto.
    2. **Consecuencias Operativas**: Qué pasa si no se interviene a tiempo el equipo (ej. daño al eje del motor, parada intempestiva del molino).
    3. **Recomendaciones de Acción Inmediata**: Pasos de mantenimiento (ej. lubricación, alineación, programar cambio de rodamiento en la siguiente parada programada).
    
    Sé muy profesional y directo.
    """
    
    # Try OpenAI
    api_key_openai = os.getenv("OPENAI_API_KEY")
    if api_key_openai:
        try:
            client = openai.OpenAI(api_key=api_key_openai)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un experto en mantenimiento predictivo y vibraciones mecánicas en minería."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.2
            )
            return response.choices[0].message.content
        except Exception as e:
            pass # Fallback to Gemini or rules
            
    # Try Gemini
    api_key_gemini = os.getenv("GEMINI_API_KEY")
    if api_key_gemini:
        try:
            genai.configure(api_key=api_key_gemini)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            pass # Fallback to rule-based
            
    # Professional Rule-based fallback if no API key is available (ensures demo NEVER fails)
    return get_rule_based_explanation(machine_name, telemetry, prediction, severity)

def get_rule_based_explanation(machine_name: str, telemetry: dict, prediction: str, severity: str) -> str:
    rms = telemetry.get("rms", 0.0)
    kurtosis = telemetry.get("kurtosis", 0.0)
    temp = telemetry.get("temperature", 0.0)
    
    if prediction == "Normal":
        return f"""### Reporte de Condición: {machine_name}
**Diagnóstico**: Normal (Condición Estable)
**Análisis**: El rodamiento se encuentra operando dentro de los parámetros de diseño. El valor RMS de vibración ({rms} g) y la curtosis ({kurtosis}) están en niveles basales. La temperatura de rodamiento ({temp}°C) es óptima.
**Recomendaciones**:
1. Continuar con la rutina periódica de lubricación programada.
2. Programar la siguiente inspección visual e inspección por ultrasonido en 30 días."""

    elif prediction == "Inner_Race":
        return f"""### Reporte de Condición: {machine_name}
**Diagnóstico**: Falla en la Pista Interna (Severidad: {severity})
**Análisis**: Se observa un incremento en el valor RMS ({rms} g) y un factor de curtosis elevado ({kurtosis}), característico de impactos cíclicos cuando los elementos rodantes pasan sobre un defecto localizado en la pista interna. La temperatura ({temp}°C) muestra un leve incremento térmico debido a la fricción local.
**Consecuencias**: Riesgo de fatiga severa del metal, desprendimiento de virutas (spalling) y daño permanente en el eje si la vibración aumenta.
**Recomendaciones**:
1. Inspeccionar la calidad del lubricante para verificar la ausencia de partículas metálicas.
2. Monitorear diariamente la tendencia del valor RMS.
3. Programar el reemplazo del rodamiento dentro de las próximas 48-72 horas de operación en una ventana de mantenimiento."""

    elif prediction == "Outer_Race":
        return f"""### Reporte de Condición: {machine_name}
**Diagnóstico**: Falla en la Pista Externa (Severidad: {severity})
**Análisis**: El indicador de impacto curtosis ({kurtosis}) y el valor RMS ({rms} g) muestran niveles altos críticos. Los impactos ocurren cada vez que un rodamiento pasa por el defecto en la pista externa, la cual está sujeta a mayor carga radial constante.
**Consecuencias**: Falla catastrófica inminente del rodamiento, traba mecánica del eje y parada intempestiva del activo, lo que detendría la línea de producción.
**Recomendaciones**:
1. **Acción Crítica**: Detener el equipo de forma segura y realizar intervención inmediata.
2. Inspeccionar la concentricidad del alojamiento del rodamiento (housing) antes de colocar el repuesto.
3. Cambiar el rodamiento y realizar balanceo dinámico y alineación láser del acople."""

    else: # Ball fault
        return f"""### Reporte de Condición: {machine_name}
**Diagnóstico**: Falla en Elementos Rodantes (Bolas/Rodillos) (Severidad: {severity})
**Análisis**: Se registran vibraciones inestables con RMS de {rms} g y una curtosis de {kurtosis}. La falla en las bolas genera una frecuencia modulada y dispersa a medida que giran y entran en contacto con ambas pistas, lo que suele acelerar el desgaste global del rodamiento.
**Consecuencias**: Destrucción total de la canastilla (jaula), desprendimiento de cuerpos rodantes y traba térmica.
**Recomendaciones**:
1. Verificar la alineación del motor y tensión de fajas.
2. Programar una parada de mantenimiento menor en el siguiente cambio de turno para inspección física.
3. Reemplazar el conjunto de rodamientos de apoyo de manera preventiva."""
