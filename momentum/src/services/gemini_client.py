import requests
import os

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.base_url = "https://api.gemini.com/v1"

    def get_market_data(self, symbol):
        url = f"{self.base_url}/pubticker/{symbol}"
        response = requests.get(url)
        return response.json()

    def get_account_balance(self):
        url = f"{self.base_url}/balances"
        headers = {"X-GEMINI-APIKEY": self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def place_order(self, symbol, amount, price, side):
        url = f"{self.base_url}/order/new"
        headers = {"X-GEMINI-APIKEY": self.api_key}
        data = {
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "side": side,
            "type": "exchange limit"
        }
        response = requests.post(url, json=data, headers=headers)
        return response.json()