class Player:
    """Holds player information, including the player's name, their current room, and items in inventory"""
    def __init__(self, name, current_room=None, items=[]):
        self.current_room = current_room
        self.name = name
        self.items = items