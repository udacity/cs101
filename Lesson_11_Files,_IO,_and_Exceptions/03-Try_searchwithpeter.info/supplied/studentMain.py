# This is the main file you should make changes
#
# To run this code locally and figure out how it works
# please download the code from our GitHub page
# http://udacity.github.io/cs101
# and run the server locally - python studentMain.py
#
from search import lucky_search
from crawler import crawl_web, compute_ranks

corpus, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

class LuckySearch(object):        
    def GET(self, query):
        result = lucky_search(corpus, ranks, query)
        return result

# running some tests
from test import test_suite
test_suite()
    
# This will be executed only if you run this code locally
# using a command: python studentMain.py

if __name__ == "__main__":
    import web
    app = web.application(('/(.*)', 'LuckySearch'), globals())
    corpus, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
    app.run()        