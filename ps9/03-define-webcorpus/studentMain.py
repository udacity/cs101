###
### You should define the WeCorpus class in the file webcorpus.py
###
from webcorpus import WebCorpus

print "Testing webcorpus..."
wc1 = WebCorpus()
assert isinstance(wc1.index, dict)
assert isinstance(wc1.graph, dict)
print "Finished tests."
        
