"""
So far, all we've done is package the index and graph into one object.  
This helps a little, but doesn't abstract the way we represent the web corpus from other modules. 
As a next step, we would like to make the ranks information part of the WebCorpus object.  
The ranks are closely tied to a particular crawl, so should be part of this object.

In preparation of moving ranks into the WebCorpus object, perform the following steps:

1. Modify the compute_ranks function in the crawler module in these ways:
   - Instead of taking a graph as input, it should take a WebCorpus object.
   - Instead of returning it directly, it should store the ranks in a ranks attribute of the WebCorpus object.

2. Modify crawl_web in the crawler module to return a WebCorpus object that includes ranks.

3. Modify the lucky_search and ordered_search functions in the search.py module 
   so that they do not take a ranks parameter (but instead use the ranks in the WebCorpus object).

After your changes, the provided test code below should work.
"""

from crawler import crawl_web, compute_ranks
from search import lucky_search, ordered_search

def test_engine():
    print "Testing..."
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'

    windex = crawl_web('http://udacity.com/cs101x/urank/index.html')
    # ==> removed now ranks = compute_ranks(windex.graph)
    assert lucky_search(windex, 'Hummus') == kathleen
    assert ordered_search(windex, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    assert lucky_search(windex, 'the') == nickel
    assert ordered_search(windex, 'the') == [nickel, arsenic, hummus, indexurl]
    assert lucky_search(windex, 'babaganoush') == None
    assert ordered_search(windex, 'babaganoush') == None
    print "Finished tests."

test_engine()
