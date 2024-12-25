from stock_price_tracker import StockPriceTracker
import time

tracker = StockPriceTracker(
    email="email_here",
    password="password_here",
    recipient_email="send_to_this"
)

# Add stocks to monitor
tracker.add_stock("AAPL", 150000)
tracker.add_stock("MSFT", 28000)
tracker.add_stock("GOOGL", 25000, email="other_email_here")

tracker.check_prices()
# while True:
#     tracker.check_prices()
#     time.sleep(60 * 60 * 24)
