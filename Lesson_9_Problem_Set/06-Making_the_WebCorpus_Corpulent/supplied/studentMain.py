"""
Next, we want to improve the modularity of our search engine code by making the WebCorpus abstract.

All your changes should go into the webcorpus.py file.  See the comments in that file for detailed instructions.

After your modifications are done, the provided test here should run correctly.
"""
from webcorpus import WebCorpus

def test_engine():
    print "Testing..."
    content = """This is a sample <a href="http://www.example.com">webpage</a> with 
    <a href="http://www.go.to">two links</a> that lead nowhere special.
    """
    outlinks = ["http://www.example.com", "http://www.go.to"]
    
    corpus = WebCorpus()
    assert corpus.lookup("anything") == None
    for link in outlinks:
        corpus.add_link("http://www.test.info", link)
    assert corpus._graph["http://www.test.info"] == outlinks
    corpus.add_word_occurrence("http://www.test.info", "sample")
    assert corpus._index["sample"] == ["http://www.test.info"]
    
    print "Finished tests."


test_engine()
