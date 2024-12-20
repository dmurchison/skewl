# build a function that takes a list and swaps the first and last elements
# and returns the modified list

def swapList(list):
    size = len(list)
    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp
    return
