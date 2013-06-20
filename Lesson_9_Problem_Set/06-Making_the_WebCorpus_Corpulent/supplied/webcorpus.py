"""
Next, we want to improve the modularity of our search engine code by making the WebCorpus abstract.  

The attributes index, graph, and ranks should no longer be used outside the webcorpus module.  
To indicate this, rename them following the convention of using an underscore at the beginning of 
private attributes.  (Python does not provide any mechanism for ensuring the _private attributes 
are not used outside the module; it is just a naming convention.)

Note that there is no explicit compute_ranks function, although you will internally want to use one.  
The ranks need to be available when page_rank is called, but shouldn't be recomputed each time.  
(Hint: you can invalidate the ranks whenever the graph is changed.)

The WebCorpus type should provide these operations:
"""

class WebCorpus:
    def __init__(self):
        """
        Initializes a new, empty WebCorpus.
        """


    def add_word_occurrence(self, url, keyword):
        """
        Adds an occurrence of word on url to the corpus.
        """


    def add_link(self, source, sink):
        """
        If source is not a node in the corpus, adds source as a new node.
        If sink is not a node in the corpus, adds sink as a new node.
        Adds a link from source to sink to the corpus.
        """
    
    def lookup(self, keyword):
        """
        Returns a list of urls where keyword appears in the corpus.  (If the
        keyword does not appear, returns None.)  The listed urls may be in
        any order.
        """

    def page_rank(self, url):
        """
        Returns the rank of the page url.
        """
