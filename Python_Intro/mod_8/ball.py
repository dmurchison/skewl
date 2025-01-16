import os.path

file_path = open('./IT_140/mod_8/ball.bmp', 'rb')  # Open in binary mode using 'b'


# Read image binary data
contents = file_path.read()

print('Contents of ball.bmp:\n')
print(contents)

file_path.close()
