# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name='Player1', current_room=None):
        self.current_room = current_room
        self.name = name
