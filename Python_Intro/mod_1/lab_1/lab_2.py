# Write a split_check function that returns the amount that each diner must pay to cover the cost of the meal.

# The function has 4 parameters:

# bill: The amount of the bill.
# people: The number of diners to split the bill between.
# tax_percentage: The extra tax percentage to add to the bill.
# tip_percentage: The extra tip percentage to add to the bill.
# The tax or tip percentages are optional and may not be given when calling split_check. Use default parameter values of 0.15 (15%) for tip_percentage, and 0.09 (9%) for tax_percentage. Assume that the tip is calculated from the amount of the bill before tax.

# Sample output with inputs: 25 2

# Cost per diner: 15.5
# Sample output with inputs: 100 2 0.075 0.21

# Cost per diner: 64.25

# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

''' Your solution goes here '''
from numpy import short


def split_check(bill, people, tax_percentage=0.09, tip_percentage=0.15):
    tax = bill * tax_percentage
    tip = bill * tip_percentage
    total = bill + tax + tip
    return total / people

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))


# Define a function compute_gas_volume that returns the volume of a gas given parameters pressure, temperature, and moles. Use the gas equation PV = nRT, where P is pressure in Pascals, V is volume in cubic meters, n is number of moles, R is the gas constant 8.3144621 ( J / (mol*K)), and T is temperature in Kelvin.

# Sample output with inputs: 100.0 1.0 273.0
# Gas volume: 22.698481533 m^3

gas_const = 8.3144621

''' Your solution goes here '''
def compute_gas_volume(pressure, temperature, moles):
    return (moles * gas_const * temperature) / pressure

gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')

# delete the first element of a list
short_list = [1, 2, 3, 4, 5]

# Sort short_names in reverse alphabetic order.
# Sample output with input: 'Jan Sam Ann Joe Tod'
# ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']

short_names = input().split()
short_names.sort(reverse=True)
print(short_names)

