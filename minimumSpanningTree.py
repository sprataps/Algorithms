'''
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in
a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
Vertices are represented as unique strings.
'''
def minimumSpanningTree(graph):
    if not graph or len(graph)<=2:
        printf("\nThe graph is insufficient to produce a MST")
        return

    vertices=graph.keys()
    print(vertices)





graph={}
