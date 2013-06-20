##################################################
#     Exercise by Sam the Great from forums!     #
##################################################
# Oh no! A superhero has just flown by 'Udacity'
# and scattered pieces of it all over the place.
# Luckily, we've recovered 3 fragments of debris
# that we can work with. Help us fix 'Udacity'!

# Write one line of Python code that uses
# only the variables fragA, fragB, and fragC 
# to satisfy the given test cases.
# If you are not sure how multiple assignments and
# string slicing works, check out the links to 
# additional tutorials in Instructor Comments
# under this exercise!

fragA, fragB, fragC = 'supercalifragilisticexpialudacious', \
                      'SUPERMAN', 'ytiroirepus'

### WRITE MULTIPLE ASSIGNMENT HERE ###
### THIS MUST BE ONE LINE ###
part1, part2, part3 = 

### TEST CASES. PRESS RUN TO TEST ###
deadline = part1 + part2[0:2] + part3[-1]
print "Test case 1 (Uday): ", deadline == 'Uday'
fixed = part1 + part2 + part3
print "Test case 2 (Udacity): ", fixed == 'Udacity'
destination = part1 + part2[-1] + part3
print "Test case 3 (Ucity): ", destination == 'Ucity'