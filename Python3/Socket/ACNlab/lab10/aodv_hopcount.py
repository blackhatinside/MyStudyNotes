import networkx as nx

class AODVNetwork:
    def __init__(self):
        self.graph = nx.Graph()
        self.explored_paths = []
        self.intermediate_nodes = set()

    def add_node(self, node_id):
        self.graph.add_node(node_id)

    def add_bidirectional_link(self, node_id1, node_id2, hop_count=1):
        self.graph.add_edge(node_id1, node_id2, hop_count=hop_count)

    def route_discovery(self, source_id, destination_id):
        self.explored_paths = []
        self.intermediate_nodes = set()
        for path in nx.all_simple_paths(self.graph, source=source_id, target=destination_id):
            hop_count = sum(self.graph[path[i]][path[i+1]]['hop_count'] for i in range(len(path)-1))
            self.explored_paths.append((path, hop_count))
            intermediate = set(path[1:-1])  # Exclude source and destination nodes
            self.intermediate_nodes.update(intermediate)

    def route_request(self, source_id, destination_id):
        self.route_discovery(source_id, destination_id)
        shortest_path = min(self.explored_paths, key=lambda x: len(x[0])) if self.explored_paths else None
        if shortest_path:
            next_hop = shortest_path[0][1]  # Next hop is the second node in the shortest path
            return {"type": "RREP", "source": source_id, "destination": destination_id, "next_hop": next_hop}, shortest_path
        else:
            return None, None

    def handle_packet(self, packet):
        if packet["type"] == "RREQ":
            print(f"Received RREQ from {packet['source']} to {packet['destination']}")
            rrep_packet, shortest_path = self.route_request(packet["source"], packet["destination"])
            if self.explored_paths:
                print("Explored Paths:")
                for path, hop_count in self.explored_paths:
                    print(f"Path (RREQ): {path}, Hop Count: {hop_count}")
                print()
                if shortest_path:
                    intermediate_nodes = shortest_path[0][1:-1]
                    print("Intermediate Nodes to Update Route Cache:", intermediate_nodes)
            if shortest_path:
                print(f"Shortest path (RREP) from {packet['source']} to {packet['destination']}:", shortest_path[0])
            return rrep_packet
        elif packet["type"] == "RREP":
            print(f"Received RREP from {packet['source']} to {packet['destination']} via {packet['next_hop']}")
        else:
            print("Unknown packet type")

# Example Usage
network = AODVNetwork()

# Define the graph connections
graph_connections = [
    (1, 2), (1, 3), (2, 5), (3, 4), (3, 5),
    (5, 6), (5, 7), (6, 8), (7, 8), (8, 9), (7, 9),
]

# Add nodes and bidirectional links based on the graph connections
for node1, node2 in graph_connections:
    network.add_node(node1)
    network.add_node(node2)
    network.add_bidirectional_link(node1, node2)

# Route Request from node 1 to node 9
rreq_packet = {"type": "RREQ", "source": 1, "destination": 8}
network.handle_packet(rreq_packet)
