# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

# Ex: If the input is:
# 0
# (or less than 0), the output is:
# No change

# Ex: If the input is:
# 45
# the output is:
# 1 Quarter
# 2 Dimes

# First, create a variable to store the change amount.
change = int(input())

# Create a variable to store the number of dollars.
dollars = change // 100
change = change % 100

# Create a variable to store the number of quarters.
quarters = change // 25
change = change % 25

# Create a variable to store the number of dimes.
dimes = change // 10
change = change % 10

# Create a variable to store the number of nickels.
nickels = change // 5
change = change % 5

# Create a variable to store the number of pennies.
pennies = change // 1

# Output the number of each coin.
if dollars == 1:
    print(dollars, "Dollar")
elif dollars > 1:
    print(dollars, "Dollars")

if quarters == 1:
    print(quarters, "Quarter")
elif quarters > 1:
    print(quarters, "Quarters")

if dimes == 1:
    print(dimes, "Dime")
elif dimes > 1:
    print(dimes, "Dimes")

if nickels == 1:
    print(nickels, "Nickel")
elif nickels > 1:
    print(nickels, "Nickels")

if pennies == 1:
    print(pennies, "Penny")
elif pennies > 1:
    print(pennies, "Pennies")

if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")

# The output should be the fewest coins possible. For example, 32 cents is one quarter and 2 pennies, not 3 dimes and 2 pennies.


