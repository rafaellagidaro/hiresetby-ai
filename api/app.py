from fastapi import FastAPI
from pydantic import BaseModel
from src.models.predict import predict
from src.explain.shap_explainer import explain_prediction

from database import engine
from models_db import Base, Candidate
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

class InputData(BaseModel):
    tempo_resposta: float
    feedback_bin: int
    score_curriculo: float

@app.get("/")
def home():
    return {"status": "Hiresetby API online"}

@app.post("/predict")
def predict_and_store(data: InputData):

    pred = predict(data.dict())

    new = Candidate(
        tempo_resposta=data.tempo_resposta,
        feedback_bin=data.feedback_bin,
        score_curriculo=data.score_curriculo,
        prediction=pred
    )

    session.add(new)
    session.commit()

    return {"prediction": pred}

@app.post("/explain")
def explain(data: InputData):
    return {"shap": explain_prediction(data.dict())}
