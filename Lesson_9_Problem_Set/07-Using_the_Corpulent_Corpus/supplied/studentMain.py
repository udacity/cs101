"""
Modify the rest of the code as necessary to use the new WebCorpus class.

For this problem, you should only need to change crawler.py and search.py.
"""
###
### test.py
###

from crawler import crawl_web
from search import lucky_search, ordered_search

def test_engine():
    print "Testing..."
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'

    corpus = crawl_web('http://udacity.com/cs101x/urank/index.html')

    assert lucky_search(corpus, 'Hummus') == kathleen
    assert ordered_search(corpus, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    assert lucky_search(corpus, 'the') == nickel
    assert ordered_search(corpus, 'the') == [nickel, arsenic, hummus, indexurl]
    assert lucky_search(corpus, 'babaganoush') == None
    assert ordered_search(corpus, 'babaganoush') == None
    print "Finished tests."

test_engine()
