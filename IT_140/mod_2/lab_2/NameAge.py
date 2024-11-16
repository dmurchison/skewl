
# Create input prompts for name and age.
in_name  = input("Enter your name: ")
in_age = int(input("Enter your age: "))

# Calculate the year born and create variable.
yr_born = 2024 - int(in_age)

# Output the desired message.
print("Hello {}! You were born in {}.".format(in_name, yr_born))

# Create a program that inputs a month(string), and a day(integer) and outputs the season.

# Create input prompts for month and day.
in_month = input("Enter a month: ")
in_day = int(input("Enter a day: "))

# Make array of months.
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]

# The dates for each season are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

# Create a variable to store the season.
season = ""

# Determine the season based on the month and day.
if in_month == "March" and in_day >= 20:
    season = "Spring"
elif in_month == "April" or in_month == "May":
    season = "Spring"
elif in_month == "June" and in_day <= 20:
    season = "Spring"
elif in_month == "June" and in_day >= 21:
    season = "Summer"
elif in_month == "July" or in_month == "August":
    season = "Summer"
elif in_month == "September" and in_day <= 21:
    season = "Summer"
elif in_month == "September" and in_day >= 22:
    season = "Autumn"
elif in_month == "October" or in_month == "November":
    season = "Autumn"
elif in_month == "December" and in_day <= 20:
    season = "Autumn"
elif in_month == "December" and in_day >= 21:
    season = "Winter"
elif in_month == "January" or in_month == "February":
    season = "Winter"
elif in_month == "March" and in_day <= 19:
    season = "Winter"


# Now if the month or the date is invalid we will output an error message

return season
