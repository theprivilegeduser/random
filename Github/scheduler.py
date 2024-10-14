import schedule
import time
from quotes import get_random_quote

def daily_quote():
    print("Here's your daily motivational quote:")
    print(get_random_quote())

schedule.every().day.at("09:00").do(daily_quote)

if __name__ == "__main__":
    print("Starting daily motivational quote scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(60)
