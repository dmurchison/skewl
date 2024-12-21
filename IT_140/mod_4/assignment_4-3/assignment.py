import random
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

if lower_bound > upper_bound:
    print("Invalid input. The lower bound must be less than the upper bound.")
    exit()

# Generate the random number
random_number = random.randint(lower_bound, upper_bound)

# Have the user guess the number
user_guess = input("Guess the number: ")

# Prompts the user to input a guess between the lower and upper bounds. Include input validation to ensure that the user only enters values between the lower and upper bound.
user_guess = input("Guess the number: ")
while int(user_guess) < lower_bound or int(user_guess) > upper_bound:
    print("Invalid input. Please enter a number between the lower and upper bounds.")
    user_guess = input("Guess the number: ")

# Prints an output statement based on the guessed number. Be sure to account for each of the following situations through the use of decision branching:
# The user's guess is correct.
# The user's guess is too high.
# The user's guess is too low.

while int(user_guess) != random_number:
    if int(user_guess) > random_number:
        print("Too high.")
    else:
        print("Too low.")
    user_guess = input("Guess the number: ")
print("Correct! The number was", random_number)
