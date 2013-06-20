# By Ashwath from forums
# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# For this question, you have to define a procedure is_leap_baby 
# which takes 3 inputs - day, month and year of birth of a comic book character
# and returns True if the character born in a leap year
# and False if the character isn't born in a leap year.

# Remember, a year that is a multiple of 4 is a leap year. 
# But, this isn't always true. 
# A year that is a multiple of 100 is NOT a leap year unless it is also 
# a multiple of 400.

def is_leap_baby(day,month,year):
    #Write your code after this line.


# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!"%name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!"%name

#Test Cases

output(is_leap_baby(29,2,1996),'Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(19,6,1978),'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29,2,2000),'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29,2,1900),'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28,2,1976),'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!
