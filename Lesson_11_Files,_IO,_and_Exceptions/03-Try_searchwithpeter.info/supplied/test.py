###
### test.py
###

from crawler import crawl_web, compute_ranks
from search import lucky_search, ordered_search

def test_suite():
    print "Testing...\n"
    from studentMain import LuckySearch
    index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
    ranks = compute_ranks(graph)
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'
    lucky = LuckySearch()
    print lucky.GET('Hummus') == kathleen
    print lucky.GET('the') == nickel
    print lucky.GET('babaganoush') == "Try searchwithpeter.info."
    print "\nFinished tests."
