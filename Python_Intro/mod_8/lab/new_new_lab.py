# Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method.
# The input file contains an unsorted list of number of seasons followed by the corresponding TV show.
# Your program should put the contents of the input file into a dictionary where the number of seasons are the keys,
# and a list of TV shows are the values (since multiple shows could have the same number of seasons).

# Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt,
# separating multiple TV shows associated with the same key with a semicolon (;).
# Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.

file_name = input()
with open(file_name, 'r') as file:
    lines = file.readlines()

data = []
for i in range(0, len(lines), 2):
    key = int(lines[i].strip())
    show = lines[i + 1].strip()
    data.append((key, show))

show_dict = {}
for key, show in data:
    if key in show_dict:
        show_dict[key].append(show)
    else:
        show_dict[key] = [show]

def sort_by_seasons(show_dict):
    formatted_dict = {key: "; ".join(shows) for key, shows in show_dict.items()}
    with open('output.txt', 'w') as file:
        for key, shows in sorted(formatted_dict.items()):
            file.write(f"{key}: {shows}\n")

def sort_by_titles(show_dict):
    all_shows = []
    for shows in show_dict.values():
        all_shows.extend(shows)

    all_shows_sorted = sorted(all_shows)

    with open('output_titles.txt', 'w') as file:
        for show in all_shows_sorted:
            file.write(f"{show}\n")

sort_by_seasons(show_dict)
sort_by_titles(show_dict)
