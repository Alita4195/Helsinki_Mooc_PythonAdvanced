# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    year_list = []  # Initialize an empty list to store the years

    for date_obj in dates:
        year_list.append(date_obj.year)  # Access the 'year' attribute and add it to the list

    year_list.sort()  # Sort the list of years in chronological order

    return year_list  # Return the sorted list of years

if __name__ == "__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)
    
    dates = [date1, date2, date3]  # Define the 'dates' list after creating the date objects
    years = list_years(dates)  # Call the function and get the list of years
    print(years)  # Print the list of years in chronological order
