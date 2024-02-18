
# Initialize total rainfall variable
total_rainfall_inches = 0

# Ask user for the number of years
num_years = int(input("Enter the number of years: "))

# Calculate the number of months
num_months = num_years * 12

# Create list of month names
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Outer loop for the years
for year in range(1, num_years + 1):
    # Inner loop for months
    for month in months:
        # Ask user for rainfall in each month
        monthly_rainfall_inches = int(input(f"Enter the amount of rainfall in inches for {month} of Year {year}: "))
        # Add each month’s rainfall to the total
        total_rainfall_inches += monthly_rainfall_inches

# Calculate the average rainfall per month
average_monthly_rainfall_inches = total_rainfall_inches / num_months

# Print results
print(f"The number of months is: {num_months}.")
print(f"The total rainfall is: {total_rainfall_inches} inches.")
print(f"The average rainfall per month is: {average_monthly_rainfall_inches} inches.")
