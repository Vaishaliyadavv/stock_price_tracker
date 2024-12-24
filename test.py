import StockPriceTracker
import time

# Initialize tracker with test email credentials
tracker = StockPriceTracker(
    email="emai_here",
    password="put_your_password_here",
)

# Add test stocks
tracker.add_stock(ticker="TATAMOTORS.NS", desired_price=100000,
                  recipient_email="on28vaishali@gmail.com")
tracker.add_stock(ticker="AAPL", desired_price=120000,
                  recipient_email="on28vaishali@gmail.com")
# add more stocks .....

while True:
    tracker.check_prices()
    time.sleep(60 * 60 * 24)
