class Bear(object):
    """Represents a bear!"""
    def __init__(self, name):
        self.name = name

    def eat(self, victim):
        print "Yummy! " + victim.name + " tastes good..."
        
class GrizzlyBear(Bear):
    """Represents a GrizzlyBear, which is a type of bear that can knock down trees."""

    def knock_down_tree(self):
        print "Timber!"

    def chase(self, victim):
        if victim.up_tree:
            self.knock_down_tree()
            victim.up_tree = False
        self.eat(victim)
        
class DiscerningBear(GrizzlyBear):
    """Represents a DiscerningBear that does not like to eat humans named Dave"""
    pass