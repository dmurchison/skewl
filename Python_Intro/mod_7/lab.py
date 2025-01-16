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

