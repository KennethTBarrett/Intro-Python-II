from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Adding items to the rooms.
room['outside'].items = [None]
room['foyer'].items = ['sword', 'lamp', 'knife']
room['overlook'].items = ['rock']
room['narrow'].items = ['torch', 'scythe']
room['treasure'].items = ['gold', 'jewels', 'jewelry']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please enter your name: ')  # Take user input for name.
player = Player(name=name, current_room=room['outside'])
print(f'{name}, welcome to the adventure game!')
print('*' * 75)  # For improved readability

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Getting input of cardinal direction, changing to caps.
answer = ''  # Empty string.

while answer != 'Q':  # While the answer isn't 'Q'
    print(player.current_room)  # Print room information of current room.
    print('=' * 70)  # For improved readability.
    # Get user input, make uppercase.
    answer = input('What direction should I take? [N/S/E/W]: ').split()
    print('-' * 55)  # For improved readability.

    # Movement / one word.
    if len(answer) == 1:
        answer = answer[0].upper()
        if answer == 'N':  # If the answer is north...
            if hasattr(player.current_room, 'n_to'):  # If N room exists...
                player.current_room = player.current_room.n_to  # Make the move.
            else:
                print('Invalid Direction!')  # Otherwise, print error.
                print('=-' * 25)  # For improved readability.
        elif answer == 'S':  # If the answer is south...
            if hasattr(player.current_room, 's_to'):  # If S room exists...
                player.current_room = player.current_room.s_to  # Make the move.
            else:
                print('Invalid Direction!')  # Otherwise, print error.
                print('=-' * 25)  # For improved readability.
        elif answer == 'E':  # If the answer is east...
            if hasattr(player.current_room, 'e_to'):  # If E room exists...
                player.current_room = player.current_room.e_to  # Make the move.
            else:
                print('Invalid Direction!')  # Otherwise, print error.
                print('=-' * 25)  # For improved readability.
        elif answer == 'W':  # If the answer is west...
            if hasattr(player.current_room, 'w_to'):  # If W room exists...
                player.current_room = player.current_room.w_to  # Make the move.
            else:
                print('Invalid Direction!')  # Otherwise, print error.
                print('=-' * 25)  # For improved readability.
        elif answer == 'Q':  # If the user wants to quit...
            exit  # Quit the game.
        elif answer == "I":
            print('Current user inventory:')
            if player.items:
                print([item.upper() for item in player.items])
            else:
                print('Inventory is empty!')
            print('=-' * 25)
        elif answer not in ['N', 'S', 'E', 'W', 'Q', 'I']:
            print('Invalid cardinal direction!')
            print('=' * 70)  # For improved readability.
    # Actions / two words.
    elif len(answer) == 2:  # If there's two words...
        if answer[0].lower() in ['get', 'take']:  # If it's a valid 'take' command...
            if answer[1].lower() in player.current_room.items:  # Confirm the item is in the room.
                player.items.append(answer[1].lower())  # Append to the player inventory.
                player.current_room.items.remove(answer[1].lower())  # Remove from room inventory.
                print(Item.on_take(item=answer[1].lower()))
            elif answer[1].lower() not in player.current_room.items:  # If not in room...
                print('Item does not exist in this room!')  # Print error.
                print('=-' * 25)  # For improved readability.
        # If command is drop + item exists in our player items...
        elif answer[0].lower() == 'drop' and answer[1].lower() in player.items:
            player.items.remove(answer[1].lower())  # Remove that item from inventory.
            player.current_room.items.append(answer[1].lower())
            print(Item.on_drop(answer[1].lower()))
        # If command is drop + item does not exist in our inventory.
        elif answer[0].lower() == 'drop' and answer[1].lower() not in player.items:
            print("You don't have that item in your inventory to drop!")  # Print error.
            print('=-' * 25)  # For improved readability.
        else:
            print(f'{answer[1]} is not in {player.current_room.name}')  # Print error.
            print('=-' * 25)  # For improved readability.
    else:
        print('You have entered an invalid command!')
        print('=-' * 25)  # For improved readability.
