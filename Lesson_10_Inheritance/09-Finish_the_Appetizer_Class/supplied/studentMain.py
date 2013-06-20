# Please edit the Appetizer class in dish.py

from dish import MainDish, Appetizer

friedpython = Appetizer("Fried Python", 101.30, serves=23)
callamari = Appetizer("Call-a-Mari", 7.95, serves=3, vegetarian=True)
bitburger = MainDish("Bit Burger", 0.13, description="Barely an eigth of a byte")
brocolliburger = MainDish("Brocolli Burger", 9.95, vegetarian=True, sides=2)
print friedpython
print callamari
print bitburger
print brocolliburger