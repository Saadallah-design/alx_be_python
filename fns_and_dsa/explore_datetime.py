# starting with importing the time module
# changed import style
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

def calculate_future_date():
    # function to get Input and Calculate
    try:
        added_days = int(input("Enter the number of days to add: "))
    except ValueError:
        
        print("Invalid input. Please enter a whole number.")
        return # exit the function if input is invalid
    
    current_date2 = datetime.now()
    time_delta = timedelta(days=added_days)
    
    # calculating the future date
    future_date =  current_date2 + time_delta

    print(future_date.strftime("%Y-%m-%d"))


# calling the functions
display_current_datetime()
calculate_future_date() 


