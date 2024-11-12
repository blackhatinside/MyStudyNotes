# Algorithms

Dijkstra's and Prim's algorithms are similar in that they both use a greedy approach and operate on graphs, but they are designed for different purposes and work in slightly different ways.
Dijkstra's Algorithm:

    Purpose: Finds the shortest path from a source vertex to all other vertices in a graph.
    How it works: It starts at the source vertex and explores the graph by repeatedly choosing the next vertex with the smallest known distance from the source. It then updates the shortest distances to its neighbors and continues until all vertices have been visited.
    Graph Type: Can work with weighted, directed and undirected graphs. It requires the graph's edge weights to be non-negative.
    Output: Shortest path tree (from the source to all other vertices).

Prim's Algorithm:

    Purpose: Finds a minimum spanning tree (MST) of a graph, which is a tree that connects all vertices with the minimum possible total edge weight.
    How it works: It starts with an arbitrary vertex and grows the MST by repeatedly adding the edge with the smallest weight that connects a vertex in the MST to a vertex outside the MST. This process continues until all vertices are included in the tree.
    Graph Type: Works on undirected, weighted graphs.
    Output: Minimum spanning tree (a subset of edges that connects all vertices with the minimum total weight).

Key Differences:

    Goal:
        Dijkstra: Shortest paths from a source to all vertices.
        Prim: Minimum spanning tree connecting all vertices.

    Edge Selection:
        Dijkstra: Chooses the smallest known distance from the source to explore.
        Prim: Chooses the smallest edge connecting the tree to a new vertex.

    Graph Structure:
        Dijkstra: Works on any graph with non-negative weights, directed or undirected.
        Prim: Specifically for undirected, connected graphs.

    Output:
        Dijkstra: Shortest path distances from the source to all vertices.
        Prim: Minimum spanning tree connecting all vertices.

Similarities:

    Both use a greedy approach.
    Both can be implemented using priority queues (heaps) to optimize performance.
