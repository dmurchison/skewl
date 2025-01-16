'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)




# Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or
# 3E. Print a space after each seat.

# Sample output with inputs: 2 3
# 1A 1B 1C 2A 2B 2C

num_rows = 2
num_cols = 3
row = 1
while row <= num_rows:
    # breakpoint()
    col = 'A'
    while col < chr(ord('A') + num_cols):
        print('{}{}'.format(row, col), end=' ')
        col = chr(ord(col) + 1)
    row = row + 1
print()

user_input = input('Enter phone number:\n')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    #FIXME: Add remaining elif branches
    elif ('d' <= character <= 'f') or ('D' <= character <= 'F'):
        phone_number += '3'
    elif ('g' <= character <= 'i') or ('G' <= character <= 'I'):
        phone_number += '4'
    elif ('j' <= character <= 'l') or ('J' <= character <= 'L'):
        phone_number += '5'
    elif ('m' <= character <= 'o') or ('M' <= character <= 'O'):
        phone_number += '6'
    elif ('p' <= character <= 's') or ('P' <= character <= 'S'):
        phone_number += '7'
    elif ('t' <= character <= 'v') or ('T' <= character <= 'V'):
        phone_number += '8'
    elif ('w' <= character <= 'z') or ('W' <= character <= 'Z'):
        phone_number += '9'
    else:
        phone_number += '?'

print('Numbers only: {}'.format(phone_number))
