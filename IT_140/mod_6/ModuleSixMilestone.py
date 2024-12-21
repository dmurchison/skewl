# Duncan Murchison

rooms = {
        'Great Hall': {'South': 'Bedroom', 'item': 'Sword'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# The main loop
def main():
    """The main loop for the text game.
    """
    current_room = 'Great Hall'
    # The game loop
    while current_room != 'Exit':
        print(f'You are in the {current_room}')
        move = input('Which direction would you like to go? (North, South, East, West, or Exit): ')
        move = move.capitalize() # This is to make sure that the input matches the keys in the dictionary
        if move in rooms[current_room]:
            current_room = rooms[current_room][move]
        elif move == 'Exit':
            current_room = 'Exit'
        else:
            print('Invalid command. Please try again.')
    print('Goodbye!')



if __name__ == '__main__': # This is the entry point for the program, in other words, __name__ is the name of the module that is being run as the main program. If the module is imported, then __name__ is the name of the module.
    main()


