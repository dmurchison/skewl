# Duncan Murchison

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
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

if __name__ == '__main__': # This is the entry point for the program
    main()


