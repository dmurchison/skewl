# Breaks and Continues

# Breaks
from os import replace
from xml.etree.ElementInclude import include


empanada_cost = 3
taco_cost = 4

user_money = 25

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('${} buys {} empanadas and {} tacos without change.'
        .format(meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')


# Continues
empanada_cost = 3
taco_cost = 4

user_money = 25

num_diners = 2

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue # Skip to next iteration

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('${} buys {} empanadas and {} tacos without change.'.format(meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')



# "Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat
# the sequence. Create a for loop that compares the two strings. For each match, add one point to user_score. Upon a
# mismatch, end the game.

# Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
# User score: 4

user_score = 0
simon_pattern = 'zZFRDS'
user_pattern  = 'zZFRDS'

for i in range(len(simon_pattern)):
    if simon_pattern[i] == user_pattern[i]:
        user_score += 1
    else:
        break

# Given a line of text as input, output the number of characters excluding spaces, periods, or commas
# Sample input: Huckleberry, Finn, by Mark Twain.

# Sample output: 25

text = "Huckleberry, Finn, by Mark Twain."

count = 0
for char in text:
    if char not in (' ', '.', ','):
        count += 1

print(count)

# Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it
# stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .

inp = 'mypassword'
# without using the replace method
new_password = ''
for char in inp:
    if char == 'i':
        new_password += '!'
    elif char == 'a':
        new_password += '@'
    elif char == 'm':
        new_password += 'M'
    elif char == 'B':
        new_password += '8'
    elif char == 'o':
        new_password += '.'
    else:
        new_password += char

# now with replace method
new_password = inp.replace('i', '!').replace('a', '@').replace('m', 'M').replace('B', '8').replace('o', '.')
print(new_password + 'q*s')

triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for i in range(1, triangle_height + 1):
    print((triangle_char + ' ') * i)


# Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in
# the example below. The program repeats until the input string is quit and disregards the integer input that follows.

# Ex: If the input is:

# apples 5
# shoes 2
# quit 0
# the output is:

# Eating 5 apples a day keeps the doctor away.
# Eating 2 shoes a day keeps the doctor away.

user_input = input()
while 'quit' not in user_input:
    user_input = user_input.split()
    print('Eating {} {} a day keeps the doctor away.'.format(user_input[1], user_input[0]))
    user_input = input()

# what else can I use besides split? 
# now without using split
user_input = input()
while 'quit' not in user_input:
    space = user_input.find(' ')
    print('Eating {} {} a day keeps the doctor away.'.format(user_input[space + 1:], user_input[:space]))
    user_input = input()
