# Module 3 Part 2

# ask user to input the time in hours
current_time = int(input("Enter the current time in hours (0-23): "))

# ask user to input the time until alarm goes off
hours_until_alarm = int(input("Enter the number of hours until the alarm goes off: "))

# Calculate the alarm time on a 24-hour clock
alarm_time = (current_time + hours_until_alarm) % 24

# Print result
print(f"The alarm will go off at {alarm_time}:00.")

