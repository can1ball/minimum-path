from collections import defaultdict

"""Codes from Mr. Badica laboratories, changed to fit the problem"""

# This class represents a graph
class Graph:

    """A graph connects nodes (vertices) by edges (links).  Each edge can also
    have a length associated with it.  The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C.
    You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B.  'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict or {}
    
    def add_edge(self, src, dest, distance=1):
        """Add a link from source and destination of given distance, the distance is 1 by default."""
        self.connect(src, dest, distance)
        self.connect(dest, src, distance)

    def connect(self, src, dest, distance):
        """Add a link from source to destionation of given distance, in one direction only."""
        self.graph_dict.setdefault(src, {})[dest] = distance

    def get(self, src, dest=None):
        """Return source link distance or a dict of {node: distance} entries.
        .get(source,destination) returns the distance or None;
        .get(source) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(src, {})
        if dest is None:
            return links
        else:
            return links.get(dest)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

# This represents a node from a graph 
class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of). Note that this node contains the path cost
    (also known as g) to reach the node."""
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost, f = g + h

    def __lt__(self, other):
        """Override operator <"""
        return self.f < other.f

    def __eq__(self, other):
        """Override operator =="""
        return self.name == other.name

    def __repr__(self):
        """Override print function"""
        return ('({0},{1})'.format(self.name, self.f))