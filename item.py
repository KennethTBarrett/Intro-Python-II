class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item):
        self.item = item
        return f"You have picked up {item.upper()}."
    
    def on_drop(self, item):
        self.item = item
        return f"You have dropped {item.upper()}."