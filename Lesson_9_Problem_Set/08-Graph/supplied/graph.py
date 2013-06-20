"""
Graph module.
"""

class Graph(object):
    """
    Represents a directed graph.
    """

    def __init__(self):
        """
        Initializes the Graph to an empty graph with no nodes or edges.
        """

    def add_node(self, node):
        """
        If node is already in the graph, returns False and does not modify the graph.
        Otherwise, adds node to the graph and returns True.
        """

    def has_node(self, node):
        """
        Returns True if node is a node in the graph.
        """


    def add_edge(self, node1, node2):
        """
        Requires: node1 and node2 are nodes in self.
        Modifies: self
        Adds an edge from node1 to node2 to self.
        """

    def get_nodes(self):
        """
        Returns a frozenset containing the nodes in the graph.
        """

    def get_outlinks(self, node):
        """
        Requires: node is a node in self.
        Returns a frozenset of the nodes to which node is connected.
        """

    def get_inlinks(self, target):
        """
        Requires: node is a node in self.
        Returns a set of the nodes that are connected by and edge to node.
        """
    
    def __str__(self):
        """
        Returns a string representation of the graph. 
        """

