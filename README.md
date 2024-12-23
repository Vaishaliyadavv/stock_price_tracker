# Stock Price Tracker 📉💰

A Python-based project that allows you to track the prices of stocks in real-time and receive email notifications when a stock price falls below a specified threshold. The program uses the `yfinance` library to fetch stock data and `smtplib` to send email alerts.

---

## Features ✨

- **Multiple Stocks Monitoring**: Monitor several stocks simultaneously by specifying their ticker symbols and target prices.
- **Email Alerts**: Get notified by email when any stock’s price falls below your desired value.
- **Real-Time Stock Data**: Uses Yahoo Finance to fetch live stock data.
- **Customizable Alerts**: Easily add or update stock tickers and target prices.
- **Automatic Checks**: Periodically checks the stock prices at regular intervals (e.g., hourly).

---

## How It Works 🛠️

1. **Set Up Stocks**: Define the stock tickers you want to monitor along with your desired price threshold.
2. **Fetch Stock Data**: The program uses the `yfinance` library to get real-time stock price information.
3. **Compare Prices**: When the price of a stock drops below your desired price, an email is sent to notify you.
4. **Email Notification**: The `smtplib` library sends an email to the specified recipient whenever a stock meets the condition.

