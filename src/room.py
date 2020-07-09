# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        currentname = f"Current room: {self.name}"
        currentdesc = f"Room Description: {self.description}"
        items_in_room = f"Items in Room: {self.items}"
        return currentname + "\n" + currentdesc + "\n" + items_in_room
