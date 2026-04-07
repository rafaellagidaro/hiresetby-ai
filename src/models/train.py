from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from src.config import MODEL_PATH

def train_model(df):

    X = df[['tempo_resposta', 'feedback_bin', 'score_curriculo']]
    y = df['status_bin']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=200)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    return model.score(X_test, y_test)
