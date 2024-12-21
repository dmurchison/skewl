# Duncan Murchison

def show_instructions():
    """Prints the instructions for the game.
    """
    print('Welcome to the text-based game!')
    print('You will be in a series of rooms and you will need to navigate through the mall, collecting items from styled before your date!')
    print('You can move in the following directions: North, South, East, West, or Exit.')
    print('Add to inventory: get "item name"')
    print('Good luck!')

rooms = {
    'Mall Food Court': {'South': 'Bottoms Store', 'North': 'Shoes Store', 'East': 'Makeup Store', 'West': 'Accessories Store'},
    'Bottoms Store': {'North': 'Mall Food Court', 'East': 'Tops Store', 'item': 'jeans'},
    'Tops Store': {'West': 'Bottoms Store', 'item': 'blouse'},
    'Cinema': {'South': 'Makeup store', 'item': 'your date'},
    'Makeup Store': {'North': 'Cinema', 'West': 'Mall Food Court', 'item': 'lipstick'},
    'Designer Store': {'West': 'Shoes Store', 'item': 'bag'},
    'Shoes Store': {'South': 'Mall Food Court', 'East': 'Designer Store', 'item': 'heels'},
    'Accessories Store': {'East': 'Mall Food Court', 'item': 'earrings'},
}



def main():
    """The main loop for the text game.
    """
    current_room = 'Mall Food Court'
    inventory = []
    # The game loop
    while current_room != 'Exit':
        # Check if the game is over
        if current_room == 'Cinema' and len(inventory) < 3:
            print('You do not have enough items to go on a date, you lose!')
            current_room = 'Exit'
            break
        elif current_room == 'Cinema' and len(inventory) >= 3:
            print('You have collected enough items to go on a date, you win!')
            current_room = 'Exit'
            break
        print(f'You are in the {current_room} \n')
        print(f'You have the following items: {inventory} \n')
        print(f'The item in this room is: {rooms[current_room].get("item")} \n')
        print(f'Since you are in the {current_room}, you can go in the following directions: {rooms[current_room].keys()} \n')
        # Get the player's input
        move = input("choose a direction, exit, or get an item: ")
        move = move.capitalize()
        # Check if the player's input is valid
        if move in rooms[current_room]:
            current_room = rooms[current_room][move]
        elif move == 'Exit':
            current_room = 'Exit'
        # Check if the player wants to pick up an item
        elif move.startswith('Get'):
            item = move.split(' ')[1]
            # Check if the item is in the room
            if 'item' in rooms[current_room] and item == rooms[current_room]['item']:
                inventory.append(item)
                inventory = list(set(inventory))
                print(f'You have picked up the {item}')
            else:
                print('There is no item here to pick up.')
        else:
            print('Invalid command. Please try again.')
    print('Goodbye!')



if __name__ == '__main__':
    show_instructions()
    main()

