# Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable,keyword):



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


#table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
#['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

#print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

#print hashtable_get_bucket(table, "Brick")
#>>> []

#print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

