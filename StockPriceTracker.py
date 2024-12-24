import yfinance as yf
import smtplib
import datetime


class StockPriceTracker:
    def __init__(self, email, password):
        """
        Initializes the tracker with email credentials.
        """
        self.smtp_server = "smtp.gmail.com"  # Default SMTP server
        self.smtp_port = 587  # Default SMTP port
        self.email = email
        self.password = password
        self.stocks_to_monitor = []

    def add_stock(self, ticker, desired_price, recipient_email):
        """
        Adds a stock to the monitoring list.
        """
        self.stocks_to_monitor.append({
            "ticker": ticker,
            "desired_price": desired_price,
            "email": recipient_email
        })

    def send_mail(self, stock_name, current_price, desired_price, recipient_email):
        """
        Sends an email alert for a stock.
        """
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)

            subject = f'Price Alert: {stock_name}'
            body = (
                f"The stock {stock_name} has fallen to {
                    current_price}, below your desired price of {desired_price}.\n\n"
                f"Check it out!"
            )
            msg = f"Subject: {subject}\n\n{body}"

            server.sendmail(self.email, recipient_email, msg)
            print(f"Email sent to {recipient_email} for {stock_name}")
            server.quit()
        except Exception as e:
            print(f"Failed to send email for {stock_name}: {e}")

    def check_prices(self):
        """
        Checks the prices of all monitored stocks and sends alerts if necessary.
        """
        for stock in self.stocks_to_monitor:
            ticker = stock["ticker"]
            desired_price = stock["desired_price"]
            recipient_email = stock["email"]

            try:
                stock_data = yf.Ticker(ticker)
                history = stock_data.history(period="1d")

                if history.empty or "Close" not in history:
                    print(f"No data available for {ticker}")
                    continue

                current_price = history["Close"].iloc[-1]
                print(f"{ticker}: {current_price} (Target: {desired_price})")

                if current_price < desired_price:
                    self.send_mail(ticker, current_price,
                                   desired_price, recipient_email)
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
