x = 5
y = 18
while y >= x:
    print(y, end=' ')
    y = y - x
print(y)

# num_a = int(input('Enter first positive integer: '))
# print()

# num_b = int(input('Enter second positive integer: '))
# print()

# while num_a != num_b:
#     if num_a > num_b:
#         num_a = num_a - num_b
#     else:
#         num_b = num_b - num_a

# print('GCD is {}'.format(num_a))

entered_value = int(input())

min_value = entered_value

while entered_value > 0:
    if entered_value < min_value:
        min_value = entered_value
    entered_value = int(input())

print('Min value:', min_value, end='')

# Given positive integer num_insects, write a while loop that prints, then doubles, num_insects each iteration. Print values ≤ 100. Follow each number with a space.

num_insects = int(input())

while num_insects <= 100:
    print(num_insects, end=' ')
    num_insects = num_insects * 2

# print the factorial of a number

num = int(input())

print(num * (num - 1))
