from room import Room
from player import Player
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please enter your name: ')
player = Player(name=name, current_room=room['outside'])
print(f'{name}, welcome to the adventure game!')
print('*' * 50)  # For improved readability

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
    answer = input('What direction should I take? [N/S/E/W]: ').upper()
    print('-' * 55)  # For improved readability.
    if answer == 'N':  # If the answer is north...
        if hasattr(player.current_room, 'n_to'):  # If N room exists...
            player.current_room = player.current_room.n_to  # Make the move.M
    elif answer == 'S':  # If the answer is south...
        if hasattr(player.current_room, 's_to'):  # If S room exists...
            player.current_room = player.current_room.s_to  # Make the move.
    elif answer == 'E':  # If the answer is east...
        if hasattr(player.current_room, 'e_to'):  # If E room exists...
            player.current_room = player.current_room.e_to  # Make the move.
    elif answer == 'W':  # If the answer is west...
        if hasattr(player.current_room, 'w_to'):  # If W room exists...
            player.current_room = player.current_room.w_to  # Make the move.
    elif answer == 'Q':  # If the user wants to quit...
        exit  # Quit the game.
    elif answer not in ['N', 'S', 'E', 'W', 'Q']:
        print('Invalid cardinal direction!')
        print('=' * 70)  # For improved readability.
