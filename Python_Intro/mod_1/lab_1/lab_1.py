# In order for a player to navigate your game, you will need to develop a function or functions using Python script. Your function or functions should do the following:
# Show the player the different commands they can enter (such as “go North”, “go West”, and “get [item Name]”).
# Show the player’s status by identifying the room they are currently in, showing a list of their inventory of items, and displaying the item in their current room.

# You could make these separate functions or part of a single function, depending on how you prefer to organize your code.
#Sample function showing the goal of the game and move commands
def show_instructions():
    #print a main menu and the commands
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

#In this solution, the player’s status would be shown in a separate function.
#You may organize your functions differently.

# Next, begin developing a main function in your code. The main function will contain the overall gameplay functionality. Review the Project Two Sample Text Game Flowchart, located in the Supporting Materials section, to help you visualize how main() will work.
# For this step, simply add in a line of code to define your main function, and a line at the end of your code that will run main(). You will develop each of the pieces for main() in Steps #4–7.

def main():
    pass

# In main(), create a dictionary linking rooms to one another and linking items to their corresponding rooms. The game needs to store all of the possible moves per room and the item in each room in order to properly validate player commands (input). This will allow the player only to move between rooms that are linked or retrieve the correct item from a room. Use your storyboard and map from Project One to help you create your dictionary.
# Here is an example of a dictionary for a few of the rooms from the sample dragon text game.
#A dictionary linking a room to other rooms
#and linking one item for each room except the Start room (Great Hall) and the room containing the villain
rooms = {
    'Great Hall' : { 'South' : 'Bedroom', 'North': 'Dungeon', 'East' : 'Kitchen', 'West' : 'Library' },
    'Bedroom' : { 'North' : 'Great Hall', 'East' : 'Cellar', 'item' : 'Armor' },
    'Cellar' : { 'West' : 'Bedroom', 'item' : 'Helmet' },
    'Dining Room' : { 'South' : 'Kitchen', 'item' : 'Dragon' } #villain
}
#The same pattern would be used for the remaining rooms on the map.

