import requests

BASE_URL = "https://api.coingecko.com/api/v3"


def get_btc_data(vs_currency="usd"):
    """
    Fetch Bitcoin market data from CoinGecko API.

    Parameters:
        vs_currency (str): currency for price (default: usd)

    Returns:
        dict: bitcoin data (price, market_cap, volume, change_24h)
        None: if request fails
    """

    endpoint = f"{BASE_URL}/coins/markets"

    params = {
        "vs_currency": vs_currency,
        "ids": "bitcoin"
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)

        # Raise error kalau status bukan 200
        response.raise_for_status()

        data = response.json()

        if not data:
            print("No data received from API")
            return None

        btc = data[0]

        result = {
            "price": btc.get("current_price"),
            "market_cap": btc.get("market_cap"),
            "volume": btc.get("total_volume"),
            "change_24h": btc.get("price_change_percentage_24h")
        }

        return result

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch data: {e}")
        return None


# 🔍 Testing (only runs if file executed directly)
if __name__ == "__main__":
    btc_data = get_btc_data()

    if btc_data:
        print("Bitcoin Data:")
        for key, value in btc_data.items():
            print(f"{key}: {value}")