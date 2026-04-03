import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("data/btc_live.csv")

# convert time ke datetime
df["time"] = pd.to_datetime(df["time"])

# sort biar rapi
df = df.sort_values("time")

# plot harga
plt.figure(figsize=(10,5))
plt.plot(df["time"], df["price"])

plt.title("Bitcoin Price Over Time")
plt.xlabel("Time")
plt.ylabel("Price (USD)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()