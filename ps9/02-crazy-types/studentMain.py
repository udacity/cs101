def crazy(a, b, c): # don't write code like this!
    return not type(a) == type(b) and type(a) == type(b + c) 

x = None
y = None
z = None

print crazy(x,y,z)
