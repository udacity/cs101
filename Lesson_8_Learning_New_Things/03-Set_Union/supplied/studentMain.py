# SPECIFICATION
# Starting from this code, implement a procedure 'union'
# that behaves as specified:
# modifies first input to become the union 
# of the first and second inputs.
# You may assume the first list is a set, that is, 
# it contains no repeated elements.
########################################################
# This is the procedure you found on the Internet
# It returns the union of two sets
def set_union(a, b):
    """return the union of two lists"""
    return list(set(a) | set(b))
    
# You have to implement this procedure
# as specified at the start
def union(a, b):



# To test, uncomment all lines 
# below except those beginning with >>>.

#a = [1,2,3]
#b = [2,4,6]
#union(a,b)
#print a 
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]