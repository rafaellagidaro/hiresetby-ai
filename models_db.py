from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Candidate(Base):
    _tablename_ = "candidates"

    id = Column(Integer, primary_key=True)
    tempo_resposta = Column(Float)
    feedback_bin = Column(Integer)
    score_curriculo = Column(Float)
    prediction = Column(Integer)
