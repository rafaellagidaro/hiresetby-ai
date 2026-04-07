import joblib
import pandas as pd
from src.config import MODEL_PATH

model = joblib.load(MODEL_PATH)

def predict(data: dict):
    df = pd.DataFrame([data])
    return int(model.predict(df)[0])
