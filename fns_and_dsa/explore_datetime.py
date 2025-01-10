# Familiarize yourself with Python’s datetime module by 
# writing a script that performs specified operations with dates and times.
from datetime import datetime, timedelta
def display_current_datetime():
    """ function to display current time"""
    current_date = datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date
def calculate_future_date(no_of_days):
    """function to display future date"""
    day = timedelta(days= no_of_days)
    future_date = display_current_datetime() + day
    print(f"Current Date and Time: {future_date.strftime('%Y-%m-%d')}")
