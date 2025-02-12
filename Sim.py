stocks = {"AAPL": 150, "GOOGL": 2800}
portfolio = {}

def buy_stock(symbol, quantity):
    if symbol in stocks:
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

def view_portfolio():
    print("Portfolio:", portfolio)

if __name__ == "__main__":
    buy_stock("AAPL", 10)
    view_portfolio()
