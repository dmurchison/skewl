# print the factorial of a number
num = -15
print(num * (num - 1))


# Write a program that lets a user enter N and that outputs N! (N factorial, meaning N*(N-1)*(N-2)*...*2*1). Hint:Use a
# loop variable i that counts from total-1 down to 1. Compare your output with some of these answers: 1:1, 2:2, 3:6, 4:24, 5:120, 8:40320.
N = -15 # N is the number entered by the user
total = N # total is the product of all the numbers from N down to 1 (N!) (for example, 5! = 5*4*3*2*1)
i = N - 1 # i is the loop variable that counts from N-1 down to 1

while i > 0: # while i is greater than 0 because we want to multiply all the numbers from N down to 1
    total = total * i # multiply total by i
    i = i - 1 # decrement i by 1
print(total) # print the final value of total



i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print('{}{}'.format(i1,i2), end=' ')
        i2 = i2 + 3
    i1 = i1 + 10
print()


