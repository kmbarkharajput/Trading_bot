from bot.validators import *

class OrderService:

    def __init__(self, client):
        self.client = client

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):
        validate_side(side)

        return self.client.place_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):
        validate_side(side)

        return self.client.place_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )