# Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. The file contains a list of words separated by commas. Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.

# Ex: If the input is:

# input1.csv
# and the contents of input1.csv are:

# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# the output is:

# hello 1
# cat 2
# man 2
# hey 2
# dog 2
# boy 2
# Hello 1
# woman 1
# Cat 1

import csv

file_name = input()
file = open(file_name, 'r')
file_reader = csv.reader(file)
word_list = []
word_freq = {}

for row in file_reader:
    for word in row:
        word_list.append(word)

for word in word_list:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

for word in word_freq:
    print(word, word_freq[word])

file.close()

