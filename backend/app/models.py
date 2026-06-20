import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "bearing_model.joblib")
ENCODER_PATH = os.path.join(os.path.dirname(__file__), "label_encoder.joblib")
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/cwru_bearing_small.csv"))

# Model training and loading helper
def get_model_and_encoder():
    if os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH):
        model = joblib.load(MODEL_PATH)
        encoder = joblib.load(ENCODER_PATH)
        return model, encoder
    
    # If model doesn't exist, train a quick Random Forest baseline
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"No se encontró el dataset de entrenamiento en: {DATA_PATH}")
        
    df = pd.read_csv(DATA_PATH)
    X = df[['rms', 'kurtosis', 'crest_factor', 'skewness', 'temperature', 'speed']]
    y = df['fault']
    
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y_encoded)
    
    # Save for future use
    joblib.dump(model, MODEL_PATH)
    joblib.dump(encoder, ENCODER_PATH)
    
    return model, encoder

def predict_bearing_fault(rms: float, kurtosis: float, crest_factor: float, skewness: float, temperature: float, speed: float):
    try:
        model, encoder = get_model_and_encoder()
    except Exception as e:
        return {"error": f"Error al cargar/entrenar el modelo: {str(e)}"}
        
    features = np.array([[rms, kurtosis, crest_factor, skewness, temperature, speed]])
    prediction_encoded = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    
    prediction = encoder.inverse_transform([prediction_encoded])[0]
    classes = encoder.classes_
    
    prob_dict = {classes[i]: float(probabilities[i]) for i in range(len(classes))}
    
    # Determine severity based on kurtosis and fault type
    severity = "Bajo"
    if prediction != "Normal":
        if kurtosis > 6.0 or rms > 0.25:
            severity = "Crítico"
        else:
            severity = "Aviso"
            
    return {
        "prediction": prediction,
        "severity": severity,
        "probabilities": prob_dict
    }
