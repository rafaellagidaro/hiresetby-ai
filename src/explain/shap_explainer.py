import shap
import joblib
import pandas as pd
from src.config import MODEL_PATH

model = joblib.load(MODEL_PATH)
explainer = shap.TreeExplainer(model)

def explain_prediction(data: dict):
    df = pd.DataFrame([data])
    shap_values = explainer.shap_values(df)
    return shap_values[1].tolist()
