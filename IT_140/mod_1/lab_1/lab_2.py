
# Write a program whose input is two integers and whose output is the two integers swapped.

# Ex: If the input is:

# 3
# 8
# the output is:

# 8 3
# Your program must define and call the following function. swap_values(num1, num2) that takes in two integers and returns them in reverse order.


''' Define your function here. '''
from math import e


def swap_values(user_val1, user_val_2):
    return user_val_2, user_val1

if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    user_val1 = int(input())
    user_val_2 = int(input())
    user_val1, user_val_2 = swap_values(user_val1, user_val_2)
    print(user_val1, user_val_2)




# Write a program with total change amount as an integer input that outputs the change using the fewest coins, one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

# Ex: If the input is:

# 0
# or less, the output is:

# no change
# Ex: If the input is:

# 45
# the output is:

# 1 quarter
# 2 dimes
# Your program must define and call the following function. The function exact_change() should return num_dollars, num_quarters, num_dimes, num_nickels, and num_pennies.
# def exact_change(user_total)

# Define your function here
def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total
    if num_dollars == 0 and num_quarters == 0 and num_dimes == 0 and num_nickels == 0 and num_pennies == 0:
        print("no change")
    if num_dollars > 1:
        print(f"{num_dollars} dollars")
    elif num_dollars == 1:
        print(f"{num_dollars} dollar")
    if num_quarters > 1:
        print(f"{num_quarters} quarters")
    elif num_quarters == 1:
        print(f"{num_quarters} quarter")
    if num_dimes > 1:
        print(f"{num_dimes} dimes")
    elif num_dimes == 1:
        print(f"{num_dimes} dime")
    if num_nickels > 1:
        print(f"{num_nickels} nickels")
    elif num_nickels == 1:
        print(f"{num_nickels} nickel")
    if num_pennies > 1:
        print(f"{num_pennies} pennies")
    elif num_pennies == 1:
        print(f"{num_pennies} penny")
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Type your code here.
    
