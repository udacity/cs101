"""
For this question, you will create a generic Graph class 
that provides a more abstract way of representing the web graph.
All your changes should go into the graph.py file.
See the file for detailed instructions.
After your modifications are done, the provided test here should run correctly.
"""
from graph import Graph

def test_engine():
    print "Testing graph..."
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("B", "A")
    print g
    assert g.get_outlinks("A") == frozenset(["B"])
    assert len(g.get_nodes()) == 3
    assert g.get_outlinks("B") == frozenset(["A", "C"])
    assert g.get_inlinks("A") == set(["B"])
    g.add_edge("C", "A")
    assert g.get_inlinks("A") == set(["B", "C"])
    print "Finished tests."

test_engine()