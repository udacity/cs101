class Restaurant(object):
    """
    Represents a place that serves food.
    """
    def __init__(self, name):
        self.name = name

    def display(self):
        """Display the restaurant."""
        print self.name
    
    def is_yummy(self):
        return False
