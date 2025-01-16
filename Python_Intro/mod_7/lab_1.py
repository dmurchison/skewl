# Write a loop to populate the list user_guesses with a number of guesses. The variable num_guesses is the number of guesses the user will have, which is read first as an integer. Read each guess (an integer) one at a time using int(input()).

# Sample output with input:
# 3 9 5 2
# user_guesses: [9, 5, 2]

num_guesses = int(input())
user_guesses = []

''' Your solution goes here '''
for i in range(num_guesses):
    user_guesses.append(int(input()))

print('user_guesses:', user_guesses)

# Assign sum_extra with the total extra credit received given list test_grades. Full credit is 100, so anything over 100 is extra credit.

# Sample output for the given program with input: '101 83 107 90'
# Sum extra: 8
# (because 1 + 0 + 7 + 0 is 8)

user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = -999 # Initialize 0 before your loop

''' Your solution goes here '''
sum_extra = 0
for grade in test_grades:
    if grade > 100:
        sum_extra += grade - 100

print('Sum extra:', sum_extra)

# Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.

# Sample output for the given program with input: '90 92 94 95'
# 90 -> 92 -> 94 -> 95
# Note: 95 is followed by a space, then a newline.

user_input = input()
hourly_temperature = user_input.split()

''' Your solution goes here '''
# The last element should not have a ' -> ' after it
for i in range(len(hourly_temperature) - 1):
    print(hourly_temperature[i], '->', end=' ')
del hourly_temperature[-1]
# Expected output:
# 90 -> 92 -> 94 -> 95

# Print the two-dimensional list mult_table by row and column. Hint: Use nested loops.

# Sample output with input: '1 2 3,2 4 6,3 6 9':
# 1 | 2 | 3
# 2 | 4 | 6
# 3 | 6 | 9
user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

''' Your solution goes here '''
for row in mult_table:
    for i in range(len(row)):
        print(row[i], end='')
        if i < len(row) - 1:
            print(' | ', end='')
    print()

# Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

# Ex: If the input is:

# 10 -7 4 39 -6 12 2
# the output is:

# 2 4 10 12 39
# For coding simplicity, follow every output value by a space. Do not end with newline.

user_input = input() # 10 -7 4 39 -6 12 2
numbers = list(map(int, user_input.split())) # numbers is a list of integers

numbers.sort()
for number in numbers:
    if number >= 0:
        print(number, end=' ')

# Write a loop that prints each country's population in country_pop.

# Sample output with input:
# 'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800':
# China has 1365830000 people.
# India has 1247220000 people.
# United States has 318463000 people.
# Indonesia has 252164800 people.

user_input = input()
entries = user_input.split(',')
country_pop = {}

for pair in entries:
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }

''' Your solution goes here '''
for country, pop in country_pop.items():
    print(f'{country} has {pop} people.')

# Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

# Ex: If the input is:

# hey hi Mark hi mark
# the output is:

# hey 1
# hi 2
# Mark 1
# hi 2
# mark 1

''' Your solution goes here '''
user_input = input()
words = user_input.split()
word_freq = {}

for word, freq in word_freq.items():
    print(f'{word} {freq}')

# Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

# Ex: If the input is:
# hey hi Mark hi mark
# The output is:
# hey 1
# hi 2
# Mark 1
# hi 2
# mark 1

user_input = input()
words = user_input.split()
word_freq = {}

''' Your solution goes here '''
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word, freq in word_freq.items():
    print(f'{word} {freq}')
# This only works for the first word in the list
# The output should be:
# hey 1
# hi 2
# Mark 1
# hi 2
# mark 1

# correct try:
user_input = input()
words = user_input.split()
word_freq = {}

''' Your solution goes here '''
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word in words:
    print(f'{word} {word_freq[word]}')

# Write a program that replaces words in a sentence. The input begins with word replacement pairs (original and replacement). The next line of input is the sentence where any word on the original list is replaced.

# Ex: If the input is:

# automobile car   manufacturer maker   children kids
# The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
# the output is:

# The car maker recommends car seats for kids if the car doesn't already have one.
# You can assume the original words are unique.

''' Your solution goes here '''
# Read the word replacement pairs
user_input = input()
# Split the input into pairs of words
pairs = user_input.split()
# Create a dictionary to store the word replacements
word_replacements = {}

# Create a dictionary of word replacements
for i in range(0, len(pairs), 2):
    word_replacements[pairs[i]] = pairs[i + 1]

# Read the sentence and split it into words
sentence = input()
sentence_words = sentence.split()

# Replace the words in the sentence with the replacements
for i in range(len(sentence_words)):
    if sentence_words[i] in word_replacements:
        sentence_words[i] = word_replacements[sentence_words[i]]

print(' '.join(sentence_words))

