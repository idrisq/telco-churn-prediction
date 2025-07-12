# main.py
import pandas as pd
import joblib
import json
from fastapi import FastAPI
from src.schema import ChurnInput

# FastAPI uygulamasını başlatalım
app = FastAPI(
    title="Müşteri Kaybı (Churn) Tahmin API",
    description="Bu API, müşteri bilgilerini alarak churn olasılığını tahmin eder.",
    version="1.0"
)

# Kaydedilmiş modeli ve sütunları yükleyelim
MODEL_PATH = "models/churn_model_v1.joblib"
COLUMNS_PATH = "models/model_columns.json"

model = joblib.load(MODEL_PATH)
with open(COLUMNS_PATH, 'r') as f:
    model_columns = json.load(f)

@app.on_event("startup")
def startup_event():
    print("API Başlatıldı. Model ve Sütunlar Yüklendi.")

@app.get("/")
def read_root():
    return {"message": "Churn Tahmin API'sine Hoş Geldiniz! Tahmin için /docs adresine gidin."}

@app.post("/predict")
def predict(data: ChurnInput):
    # Gelen veriyi bir pandas DataFrame'e çevir
    input_data = pd.DataFrame([data.dict()])

    # Notebook'ta yaptığımız özellik mühendisliğini burada da yapmalıyız!
    ek_hizmetler = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    input_data['EkHizmetSayisi'] = input_data[ek_hizmetler].apply(lambda x: (x == 'Yes').sum(), axis=1)
    input_data['AylikFaturaOrani'] = input_data['MonthlyCharges'] / (input_data['TotalCharges'] + 1e-6)

    # One-Hot Encoding yap
    input_processed = pd.get_dummies(input_data).reindex(columns=model_columns, fill_value=0)

    # Tahmini yap
    prediction = model.predict(input_processed)
    probability = model.predict_proba(input_processed)

    churn_status = "Gidecek (Churn)" if prediction[0] == 1 else "Kalacak"
    churn_probability = probability[0][1] # 'Gidecek' sınıfının olasılığı

    return {
        "prediction": churn_status,
        "churn_probability": f"{churn_probability:.4f}"
    }