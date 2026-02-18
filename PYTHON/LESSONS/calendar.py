
def is_leap_year(year):
    """Check if the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    """Return the number of days in the given month and year."""
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def zeller_congruence(day, month, year):
    """Calculate the day of the week for a given date using Zeller's Congruence."""
    if month < 3:
        month += 12
        year -= 1
    k = day
    m = month
    D = year % 100
    C = year // 100
    f = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - (2 * C)
    return (f % 7 + 7) % 7  # Returns 0=Sat, 1=Sun, ..., 6=Fri

def print_calendar(year, month):
    """Display a calendar for the given year and month."""
    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    
    # Validate inputs
    try:
        year = int(year)
        month = int(month)
        if not (1 <= month <= 12):
            print("Error: Month must be between 1 and 12.")
            return
        if year < 1:
            print("Error: Year must be a positive number.")
            return
    except ValueError:
        print("Error: Year and month must be valid numbers.")
        return

    # Get first day of the month and number of days
    first_day = zeller_congruence(1, month, year)
    # Adjust for Sunday-start calendar (0=Sun, 1=Mon, ..., 6=Sat)
    first_day = (first_day + 6) % 7  # Convert: Sat(0)→6, Sun(1)→0, Mon(2)→1, ..., Fri(6)→5
    days_in_month = get_days_in_month(month, year)
    
    # Print header
    print(f"\n{month_names[month]} {year}".center(20))
    print("Su Mo Tu We Th Fr Sa")
    
    # Print leading spaces
    current_day = 0
    for i in range(first_day):
        print("  ", end=" ")
        current_day += 1
    
    # Print days
    for day in range(1, days_in_month + 1):
        print(f"{day:2}", end=" ")
        current_day += 1
        if current_day % 7 == 0:
            print()  # New line after Saturday
    
    print()  # Final newline
    print(f"Is {year} a leap year? {is_leap_year(year)}")

def main():
    """Main function to get user input and display the calendar."""
    print("Enter the year and month to display the calendar.")
    year = input("Year (e.g., 2025): ")
    month = input("Month (1-12): ")
    print_calendar(year, month)

if __name__ == "__main__":
    main()