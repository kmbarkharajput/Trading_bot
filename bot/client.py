from binance.client import Client
from bot.config import API_KEY, API_SECRET


class BinanceClient:

    def __init__(self):
        self.client = Client(
            API_KEY,
            API_SECRET,
            testnet=True
        )

    def place_order(self, **params):
        return self.client.futures_create_order(**params)