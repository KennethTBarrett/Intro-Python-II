class Room:
    """Holds room attributes, including room name, description,
       and items in room."""
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        """Prints attributes for room"""
        currentname = f"Current room: {self.name}"
        currentdesc = f"Room Description: {self.description}"
        items_in_room = f"""Items in Room: {[item.upper() if item != None else
                                           item for item in self.items]}"""
        return currentname + "\n" + currentdesc + "\n" + items_in_room
