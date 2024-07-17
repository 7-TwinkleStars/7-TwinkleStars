def calculate_day_of_week(month_name, day_in_month, year):
    # Initialize month_number with a default value
    month_number = 0

    # Convert month name to month number
    if month_name == "January":
        month_number = 13
    elif month_name == "February":
        month_number = 14
    elif month_name == "March":
        month_number = 3
    elif month_name == "April":
        month_number = 4
    elif month_name == "May":
        month_number = 5
    elif month_name == "June":
        month_number = 6
    elif month_name == "July":
        month_number = 7
    elif month_name == "August":
        month_number = 8
    elif month_name == "September":
        month_number = 9
    elif month_name == "October":
        month_number = 10
    elif month_name == "November":
        month_number = 11
    elif month_name == "December":
        month_number = 12

        # Adjust year for January and February
    if month_number <= 2:
        year -= 1

    # Calculate variations in days per month
    variation_in_days_per_month = (13 * (month_number + 1)) // 5

    # Calculate leap year days
    leap_year_days = year // 4 + year // 400

    # Calculate century days
    century_days = year // 100

    # Calculate total days
    total_days = day_in_month + variation_in_days_per_month + year + leap_year_days - century_days

    # Calculate day of the week
    day_of_week = total_days % 7

    # Determine day name
    if day_of_week == 0:
        day_name = "Saturday"
    elif day_of_week == 1:
        day_name = "Sunday"
    elif day_of_week == 2:
        day_name = "Monday"
    elif day_of_week == 3:
        day_name = "Tuesday"
    elif day_of_week == 4:
        day_name = "Wednesday"
    elif day_of_week == 5:
        day_name = "Thursday"
    else:
        day_name = "Friday"

    return day_name


def main():
    month_name = input("Enter the month (for example, January, February, etc.): ")
    day_in_month = int(input("Enter the day (an integer): "))
    year = int(input("Enter the year (an integer): "))
    day_name = calculate_day_of_week(month_name, day_in_month, year)
    print(f"The day of the week is {day_name}.")


if __name__ == "__main__":
    main() 
