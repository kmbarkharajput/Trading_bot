import argparse
import sys
from bot.client import BinanceClient
from bot.orders import OrderService


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    try:
        client = BinanceClient()
        order_service = OrderService(client)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.type == "LIMIT":
            if args.price is None:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            print(f"Price    : {args.price}")

            response = order_service.place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        else:
            response = order_service.place_market_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )

        print("\n========== ORDER RESPONSE ==========")

        print(
            f"Order ID      : "
            f"{response.get('orderId', 'N/A')}"
        )

        print(
            f"Status        : "
            f"{response.get('status', 'N/A')}"
        )

        print(
            f"Executed Qty  : "
            f"{response.get('executedQty', 'N/A')}"
        )

        print(
            f"Average Price : "
            f"{response.get('avgPrice', 'N/A')}"
        )

        print("\nSUCCESS: Order placed successfully.")

    except Exception as e:
        print(f"\nERROR: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()