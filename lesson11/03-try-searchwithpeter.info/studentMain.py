# This is the main file you should make changes
# Modify this file to make sure that it behaves as asked in the video.
# To test your code you have to install web.py locally
# and run these files locally as well.
# If you run it locally, you can rename this file to server.py

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