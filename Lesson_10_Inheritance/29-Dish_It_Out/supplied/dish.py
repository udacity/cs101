#
# dish.py
#

class Dish(object):
    """
    Represents a food dish.
    """

    def __init__(self, name, price, description=None, vegetarian=False):
        self.name = name
        self.price = price
        self.description = description
        self.vegetarian = vegetarian
    
    def __str__(self):
        return "{name}{isveg}: {price:.2f}{desc}".format(
            name=self.name,
            desc=' (' + self.description + ')' if self.description else '',
            price=self.price,
            isveg='*' if self.vegetarian else '',
            extras = self.extras())
    
class MainDish # you need to finish this
    """
    Represents an entree (main dish).
    """

class Appetizer # you need to finish this
    """
    Represents an appetizer.
    """





