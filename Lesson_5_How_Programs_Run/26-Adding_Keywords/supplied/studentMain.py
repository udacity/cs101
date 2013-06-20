# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in 
# the correct bucket), with the correct 
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable,key,value):
    # your code here
    
    return htable  
    
    
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

#table = make_hashtable(5)
#hashtable_add(table,'Bill', 17)
#hashtable_add(table,'Coach', 4)
#hashtable_add(table,'Ellis', 11)
#hashtable_add(table,'Francis', 13)
#hashtable_add(table,'Louis', 29)
#hashtable_add(table,'Nick', 2)
#hashtable_add(table,'Rochelle', 4)
#hashtable_add(table,'Zoe', 14)
#print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

