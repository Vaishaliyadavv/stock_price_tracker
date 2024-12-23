import yfinance as yf
import smtplib
import time
import datetime

stocks_to_monitor = [
    {"ticker": "TATAMOTORS.NS", "desired_price": 600, "email": "on28vaishali@gmail.com"},
    {"ticker": "GRAVITA.NS", "desired_price": 1900, "email": "on28vaishali@gmail.com"},
    {"ticker": "INFY.NS", "desired_price": 1500, "email": "on28vaishali@gmail.com"},
    {"ticker": "TCS.NS", "desired_price": 3000, "email": "on28vaishali@gmail.com"}]


def send_mail(stock_name, current_price, desired_price, recipient_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('vaishali.yadavv09@gmail.com', 'mfqedvmolvwksrqk')

        subject = f'Price Alert: {stock_name}'
        body = f"The stock {stock_name} has fallen to {current_price}, below our desired price of {desired_price}.\n\nCheck it out!"
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('vaishali.yadavv09@gmail.com', recipient_email, msg)
        print(f"Email sent to {recipient_email} for {stock_name}")
        server.quit()
    except Exception as e:
        print(f"Failed to send email for {stock_name}: {e}")


def check_prices():
    for stock in stocks_to_monitor:
        ticker = stock["ticker"]
        desired_price = stock["desired_price"]
        recipient_email = stock["email"]

        try:
            # Fetch stock data
            stock_data = yf.Ticker(ticker)
            history = stock_data.history(period="1d")

            if history.empty or "Close" not in history:
                print(f"No data available for {ticker}")
                continue

            current_price = history["Close"].iloc[-1]
            print(f"{ticker}: {current_price} (Target: {desired_price})")

            # Check price and send email if necessary
            if current_price < desired_price:
                send_mail(ticker, current_price, desired_price, recipient_email)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")



# check_prices()
# Periodically check prices
while True:
    print(f"Checking prices at {datetime.datetime.now()}...")
    check_prices()
    time.sleep(60 * 60)  # Check every hour
