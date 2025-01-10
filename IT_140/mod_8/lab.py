# Simple file read, write, and append
# Read the file
fr = open("./IT_140/mod_8/lab.txt", "r")
print(fr.read())
fr.close()

# Write to the file
fw = open("./IT_140/mod_8/lab.txt", "w")
fw.write("This is a new line\n")
fw.close()

# Append to the file
fa = open("./IT_140/mod_8/lab.txt", "a")
fa.write("This is an appended line\n")
fa.close()

print("File read, write, and append complete.")
print("File contents:")
fr = open("./IT_140/mod_8/lab.txt", "r")

# Open file in binary mode
fb = open("./IT_140/mod_8/lab.txt", "rb")
print('\nBinary file contents:')
print(fb.read())

# To print the hexidecimal representation of a number in Python, use the hex() function.
print('\nHexidecimal representation of 42:')
bin = hex(42)

# To create a bytes object from a string, use the encode() method.
print('\nBytes object from string:')
string = 'Hello, World!'
bytes = string.encode()
print(bytes)
print(type(bytes))
# Can you create a bytes object from an integer?
# Yes, you can create a bytes object from an integer using the to_bytes() method.
print('\nBytes object from integer:')
integer = 42
bytes = integer.to_bytes(1, byteorder='big')
print(bytes)
print(type(bytes))
