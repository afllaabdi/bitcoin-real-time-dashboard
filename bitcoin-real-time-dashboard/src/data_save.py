import pandas as pd
from datetime import datetime
import os

# import dari file yang sama folder
from data_fetch import get_btc_data


FILE_PATH = "data/btc_live.csv"


def save_data():
    # ambil data dari API
    data = get_btc_data()

    if data is None:
        print("❌ Gagal ambil data")
        return

    # tambah waktu sekarang
    data["time"] = datetime.now()

    # ubah ke DataFrame
    df = pd.DataFrame([data])

    # pastikan folder data ada
    os.makedirs("data", exist_ok=True)

    # cek file sudah ada atau belum
    file_exists = os.path.isfile(FILE_PATH)

    # simpan ke CSV (append)
    df.to_csv(
        FILE_PATH,
        mode="a",
        header=not file_exists,
        index=False
    )

    print(f"✅ Saved: {data['time']} | Price: {data['price']}")


# RUN PROGRAM
if __name__ == "__main__":
    save_data()