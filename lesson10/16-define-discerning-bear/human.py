class Human(object):
    """Represents a human!"""
    def __init__(self, name):
        self.name = name
        self.up_tree = False

    def climb_tree(self):
        self.up_tree = True