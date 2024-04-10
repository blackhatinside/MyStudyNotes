import networkx as nx
import numpy as np

def bellman_ford(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    next_hop = [-1] * n

    dist[start] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in graph.neighbors(u):
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    next_hop[v] = u

    return dist, next_hop

def dijkstra_with_next_hop(graph, start):
    dist = {}
    next_hop = {}
    
    # Initialize distances and next hops
    for node in graph.nodes():
        dist[node] = float('inf')
        next_hop[node] = -1
    dist[start] = 0
    
    # Run Dijkstra's algorithm
    pq = [(0, start)]
    while pq:
        d, u = pq.pop(0)
        if d > dist[u]:
            continue
        for v in graph.neighbors(u):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                next_hop[v] = u
                pq.append((alt, v))
                pq.sort(key=lambda x: x[0])

    return dist, next_hop

if __name__ == "__main__":
    adjacency_matrix = [
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0]
    ]
    graph = nx.from_numpy_matrix(np.array(adjacency_matrix))
    
    num_nodes = len(graph)
  
    for i in range(num_nodes):
        shortest_distances, next_hop = dijkstra_with_next_hop(graph, i)
        print("Shortest paths from node", i, ":")
        for j in range(num_nodes):
            print("Node", j, ":", shortest_distances[j], "Next hop:", next_hop[j])
        print()
