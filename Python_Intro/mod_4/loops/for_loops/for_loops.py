# Write a for loop to print each contact in contact_emails.

# Sample output with inputs: 'Alf' 'alf1@hmail.com'
# mike.filt@bmail.com is Mike Filt
# s.reyn@email.com is Sue Reyn
# narty042@nmail.com is Nate Arty
# alf1@hmail.com is Alf

contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

# new_contact = input()
# new_email = input()
# contact_emails[new_contact] = new_email

# for contact in contact_emails:
#     print(contact_emails[contact], 'is', contact)

# The range function generates the numbers from 0 to 4. The for loop iterates over each number in the range and prints the number.


# Modify the program to include two-character .com names, where the second character can be a letter or a number, e.g.,
# a2.com. Hint: Add a second while loop nested in the outer loop, but following the first inner loop, that iterates through the numbers 0-9.

'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a' # This is to reset the second letter to 'a' after the first loop
    while letter2 <= 'z':  # Inner loop for letters a-z
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1) # This is to increment the second letter by 1 during the loop.
    letter2 = '0' # This is to reset the second letter to '0' after the first loop
    while letter2 <= '9':  # Inner loop for numbers 0-9
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

# The program prints all 2-letter domain names, starting with aa.com and ending with zz.com. The outer loop iterates
# over the first letter, and the inner loop iterates over the second letter. The inner loop prints the domain name and
# increments the second letter. The outer loop increments the first letter and repeats the inner loop. The program uses
# the ord() and chr() functions to convert between text and ASCII/Unicode encodings.

