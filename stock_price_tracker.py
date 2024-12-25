import time
import yfinance as yf
import smtplib
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class StockPriceTracker:
    def __init__(self, email, password, recipient_email):
        """
        Initializes the tracker with email credentials.
        """
        self.smtp_server = "smtp.gmail.com"  # Default SMTP server
        self.smtp_port = 587  # Default SMTP port
        self.email = email
        self.password = password
        self.stocks_to_monitor = []
        self.recipient_email = recipient_email

    def add_stock(self, ticker, desired_price, email=None):
        """
        Adds a stock to the monitoring list.
        """
        stock_email = email or self.recipient_email
        self.stocks_to_monitor.append({
            "ticker": ticker,
            "desired_price": desired_price,
            "email": stock_email
        })
        logging.info(f"Added stock: {ticker} with target price {
                     desired_price} for {stock_email}")

    def send_mail(self, stock_name, current_price, desired_price, recipient_email):
        """
        Sends an email alert for a stock.
        """
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)

                subject = f'Price Alert: {stock_name}'
                body = (
                    f"The stock {stock_name} has fallen to {current_price}, "
                    f"below your desired price of {
                        desired_price}.\n\nCheck it out!"
                )
                msg = f"Subject: {subject}\n\n{body}"

                server.sendmail(self.email, recipient_email, msg)
                logging.info(f"Email sent to {
                             recipient_email} for {stock_name}")
        except Exception as e:
            logging.error(f"Failed to send email for {
                          stock_name}: {e}", exc_info=True)

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
                    logging.warning(f"No data available for {ticker}")
                    continue

                current_price = history["Close"].iloc[-1]
                logging.info(f"{ticker}: Current price is {
                             current_price} (Target: {desired_price})")

                if current_price < desired_price:
                    self.send_mail(ticker, current_price,
                                   desired_price, recipient_email)
            except Exception as e:
                logging.error(f"Error fetching data for {
                              ticker}: {e}", exc_info=True)
