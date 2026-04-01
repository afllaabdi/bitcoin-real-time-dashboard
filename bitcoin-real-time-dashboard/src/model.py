import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from src.feature_engineering import create_features


def train_model():
    # =========================
    # LOAD DATA
    # =========================
    df = pd.read_csv("data/btc_live.csv")

    print("Data sebelum feature:", len(df))

    # =========================
    # FEATURE ENGINEERING
    # =========================
    df = create_features(df)

    print("Data setelah feature:", len(df))

    # =========================
    # VALIDASI DATA
    # =========================
    if len(df) < 5:
        print("❌ Data terlalu sedikit untuk modeling")
        print("👉 Jalankan dulu: python src/data_save.py (beberapa kali)")
        return None

    # =========================
    # SPLIT X dan y
    # =========================
    X = df[["lag1", "ma5", "ma10", "volatility"]]
    y = df["price"]

    # =========================
    # TRAIN TEST SPLIT
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # =========================
    # MODEL
    # =========================
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # =========================
    # EVALUASI
    # =========================
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    print("✅ MAE:", mae)

    return model


if __name__ == "__main__":
    train_model()