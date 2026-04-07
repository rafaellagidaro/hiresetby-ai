from src.data.load_data import load_data
from src.features.build_features import build_features
from src.models.train import train_model

df = load_data()
df = build_features(df)

acc = train_model(df)

print(f"Acurácia: {acc}")
