### Modify the crawler code to return a WebCorpus object.  
### You will need to add an import and modify the crawl_web function.
### After your changes, the provided test code below should work.
### You should do your modifications to the crawler.py file

from crawler import crawl_web, compute_ranks
from search import lucky_search, ordered_search
from webcorpus import WebCorpus

def test_engine():
    print "Testing..."
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'

    wcorpus = crawl_web('http://udacity.com/cs101x/urank/index.html')
    assert isinstance(wcorpus, WebCorpus)
    ranks = compute_ranks(wcorpus.graph)
    assert lucky_search(wcorpus.index, ranks, 'Hummus') == kathleen
    assert ordered_search(wcorpus.index, ranks, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    assert lucky_search(wcorpus.index, ranks, 'the') == nickel
    assert ordered_search(wcorpus.index, ranks, 'the') == [nickel, arsenic, hummus, indexurl]
    assert lucky_search(wcorpus.index, ranks, 'babaganoush') == None
    assert ordered_search(wcorpus.index, ranks, 'babaganoush') == None
    print "Finished tests."

test_engine()
