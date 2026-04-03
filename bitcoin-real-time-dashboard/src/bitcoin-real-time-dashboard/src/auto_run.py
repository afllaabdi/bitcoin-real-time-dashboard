from src.data_save import save_data
import time

INTERVAL = 10  # detik

if __name__ == "__main__":
    print("🚀 Auto data collection started...")

    while True:
        save_data()
        time.sleep(INTERVAL)