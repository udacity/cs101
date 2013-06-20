# Add the magic __str__ method to this class
# It should print out information in the following pseudoformat
# name (Owner: owner, Chef: chef)
class Restaurant(object):
    """
    Represents a place that serves food.
    """
    def __init__(self, p_name, p_owner, p_chef):
        self.name = p_name
        self.owner = p_owner
        self.chef = p_chef

    def is_yummy(self):
        """Returns True if this restaurant is yummy; otherwise, returns False."""
        return False

    def display(self):
        """Display the restaurant."""
        print self.name