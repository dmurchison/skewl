# (1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into
# separate variables. Then, output those four values on a single line separated by a space. (Submit for 2 points).

user_int = int(input("Enter integer (32 - 126):"))

user_float = float(input("Enter float:"))

user_char = input("Enter character:")

user_string = input("Enter string:")

print(user_int, user_float, user_char, user_string)

# (2) Extend to output this in reverse as well. (Submit for 2 points).

print(user_string, user_char, user_float, user_int)

# (3) Extend to convert the integer to a character by using the 'chr()' function, and output that character.
# (Submit for 2 points, so 5 points total).

print(f"{user_int} converted to a character is {chr(user_int)}")
