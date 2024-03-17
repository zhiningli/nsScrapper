import requests
from src.commons.classes.exchange_rates import ExchangeRateCache


exchange_rate_cache = ExchangeRateCache()

def get_exchange_rate():
    if exchange_rate_cache.is_data_stale():
        print("Fetching new data...")
        url = "https://v6.exchangerate-api.com/v6/c73771fa1bc10be89f2d0f28/latest/USD"
        response = requests.get(url)
        response.raise_for_status()
        exchange_rates = response.json().get("conversion_rates")
        exchange_rate_cache.update_data(exchange_rates)  # Update the cache with the new data
    else:
        print("Using cached data...")

    return exchange_rate_cache.get_data()
