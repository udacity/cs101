# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
