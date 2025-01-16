from collections import namedtuple

# Create a named tuple
Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])

chevy_impala = Car('Chevrolet', 'Impala', 31000, 305, 5)
chevy_blazer = Car('Chevrolet', 'Blazer', 29000, 193, 5)

print(Car)

# The reason people use named tuples is because they are more readable than regular tuples.

# The reason people use the `if __name__ == '__main__':` block is to prevent the code from running when the module is imported into another program.


print(10*.5)



my_name = "John"
place = "World"

# This is a string
my_string = "Hello, {} I am {}".format(place, my_name)

# This is how I would format the string in Ruby

print(my_string)

num = 1069

print("{:b}".format(num))
