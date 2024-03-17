import time

# Structure for storing the exchange rate data
class ExchangeRateCache:
    def __init__(self):
        self.timestamp = 0
        self.data = {}

    def is_data_stale(self, hours=12):
        elapsed_time = time.time() - self.timestamp
        return elapsed_time > hours * 3600

    def update_data(self, data):
        self.timestamp = time.time()
        self.data = data

    def get_data(self):
        return self.data



