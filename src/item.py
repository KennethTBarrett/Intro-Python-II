class Item:
    """Class for item attributes"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(item):
        """Returns 'take' statement when item is picked up."""
        return f"You have picked up {item.upper()}." + "\n" + ("=-=-" * 10)
    
    def on_drop(item):
        """Returns 'drop' statement when item is dropped."""
        return f"You have dropped {item.upper()}." + "\n" + ("=-=-" * 10)