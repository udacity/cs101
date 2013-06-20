# Please edit the Restaurant class in the file restaurant.py

from restaurant import Restaurant

# These are test cases

mcdowells = Restaurant("McDowell's Hamgurger Emporium", "Cleo McDowell", "Chef Queasy")


# test case:
print mcdowells.__str__() == "McDowell's Hamgurger Emporium (Owner: Cleo McDowell, Chef: Chef Queasy)"