
from stock_price_tracker import StockPriceTracker
from apscheduler.triggers.cron import CronTrigger

# Initialize the tracker
tracker = StockPriceTracker(
    email="vaishali.yadavv09@gmail.com",
    password="mfqedvmolvwksrqk",
    recipient_email="on28vaishali@gmail.com",
    cron_trigger=CronTrigger(minute="*")  # Every minute for testing
)

# Add stocks to monitor
tracker.add_stock("AAPL", 150)
tracker.add_stock("MSFT", 280)
tracker.add_stock("GOOGL", 2500)

# Start the scheduler
tracker.run_scheduler()
