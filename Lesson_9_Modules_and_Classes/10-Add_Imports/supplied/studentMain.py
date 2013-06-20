### Add your imports here:

def test_engine():
    print "Testing..."
    index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
    ranks = compute_ranks(graph)
    kathleen = 'http://udacity.com/cs101x/urank/kathleen.html'
    nickel = 'http://udacity.com/cs101x/urank/nickel.html'
    arsenic = 'http://udacity.com/cs101x/urank/arsenic.html'
    hummus = 'http://udacity.com/cs101x/urank/hummus.html'
    indexurl = 'http://udacity.com/cs101x/urank/index.html'
    # print lucky_search(index, ranks, 'Hummus')
    assert lucky_search(index, ranks, 'Hummus') == kathleen
    #print ordered_search(index, ranks, 'Hummus')
    assert ordered_search(index, ranks, 'Hummus') == [kathleen, nickel, arsenic, hummus, indexurl] 
    #print lucky_search(index, ranks, 'the')
    assert lucky_search(index, ranks, 'the') == nickel
    #print ordered_search(index, ranks, 'the')
    assert ordered_search(index, ranks, 'the') == [nickel, arsenic, hummus, indexurl]
    #print lucky_search(index, ranks, 'babaganoush')
    assert lucky_search(index, ranks, 'babaganoush') == None
    assert ordered_search(index, ranks, 'babaganoush') == None
    print "Finished tests."

test_engine()
