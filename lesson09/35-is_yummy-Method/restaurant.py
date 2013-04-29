class Restaurant(object):
    """
    Represents a place that serves food.
    """
    def __init__(self, name):
        self.name = name

    def display(self):
        """Display the restaurant."""
        print self.name
    
    # define a method is_yummy
    # that returns a boolean value of yummyness
    # for now it should always return False

