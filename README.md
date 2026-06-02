# Binance Futures Testnet Trading Bot

A simple Python CLI application for placing Market and Limit orders on Binance Futures Testnet (USDT-M).

## Setup

## 1. Create virtual environment
python -m venv venv

## 3. Activate environment
Windows:
venv\Scripts\activate
Linux:
source venv/bin/activate
## 4. Install dependencies
pip install -r requirements.txt

## Create .env file:
- Create .env file:
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret

## How to run
- Market order 
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
-- Limit order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000

## Output
- MARKET BUY BTCUSDT 0.001
Order ID: 123456789
Status: FILLED
Executed Qty: 0.001
Average Price: 105432.50
SUCCESS

- LIMIT SELL BTCUSDT 0.001 @ 120000
Order ID: 123456790
Status: NEW
Executed Qty: 0
Average Price: 0
SUCCESS
