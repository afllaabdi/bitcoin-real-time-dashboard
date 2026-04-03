import pandas as pd


def create_features(df):
    # pastikan kolom time dalam format datetime
    df["time"] = pd.to_datetime(df["time"])

    # urutkan berdasarkan waktu
    df = df.sort_values("time")

    # ==============================
    # FEATURE ENGINEERING
    # ==============================

    # 1. Return (persentase perubahan harga)
    df["return"] = df["price"].pct_change()

    # 2. Moving Average
    df["ma5"] = df["price"].rolling(window=5).mean()
    df["ma10"] = df["price"].rolling(window=10).mean()

    # 3. Lag (harga sebelumnya)
    df["lag1"] = df["price"].shift(1)
    df["lag2"] = df["price"].shift(2)

    # 4. Volatility (standar deviasi)
    df["volatility"] = df["price"].rolling(window=5).std()

    # hapus data yang ada NaN
    df = df.dropna()

    return df


# ==============================
# TEST RUN (biar bisa dijalankan langsung)
# ==============================
if __name__ == "__main__":
    try:
        # load data
        df = pd.read_csv("data/btc_live.csv")

        print("=== DATA SEBELUM FEATURE ===")
        print(df.head())

        # proses feature engineering
        df = create_features(df)

        print("\n=== DATA SETELAH FEATURE ===")
        print(df.head())

        print("\nJumlah data:", len(df))

    except FileNotFoundError:
        print("❌ File data/btc_live.csv belum ada.")
        print("👉 Jalankan dulu: python src/data_save.py")