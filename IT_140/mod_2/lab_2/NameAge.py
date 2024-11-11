
# Create input prompts for name and age.
in_name  = input("Enter your name: ")
in_age = int(input("Enter your age: "))

# Calculate the year born and create variable.
yr_born = 2024 - int(in_age)

# Output the desired message.
print("Hello {}! You were born in {}.".format(in_name, yr_born))
