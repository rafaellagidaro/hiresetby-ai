def build_features(df):
    df['status_bin'] = df['status'].map({'Respondido': 1, 'Ignorado': 0})
    df['feedback_bin'] = df['feedback_dado'].map({'Sim': 1, 'Não': 0})
    return df
