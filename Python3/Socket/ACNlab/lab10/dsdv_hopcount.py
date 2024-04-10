from graphviz import Digraph

class DSDV:
    def __init__(self):
        self.routing_table = {}
        self.seq_num = 0  # Initial sequence number

    def update_routing_table(self, node, destination, next_hop, num_hops):
        if node not in self.routing_table:
            self.routing_table[node] = {}
        
        if destination in self.routing_table[node]:
            current_next_hop, current_num_hops, current_seq_num = self.routing_table[node][destination]
            if num_hops < current_num_hops or (num_hops == current_num_hops and self.seq_num > current_seq_num):
                self.routing_table[node][destination] = (next_hop, num_hops, self.seq_num)
        else:
            self.routing_table[node][destination] = (next_hop, num_hops, self.seq_num)

    def periodic_update(self):
        self.seq_num += 1  # Increment sequence number for periodic update
        for node in self.routing_table:
            for destination, (next_hop, num_hops, seq_num) in self.routing_table[node].items():
                self.routing_table[node][destination] = (next_hop, num_hops, self.seq_num)

    def visualize_routing_table(self):
        print("Routing Tables:")
        for node in self.routing_table:
            print(f"Node: {node}")
            print("Destination\tNext Hop\tNum Hops\tSeq Num")
            for destination, (next_hop, num_hops, seq_num) in self.routing_table[node].items():
                print(f"{destination}\t\t{next_hop}\t\t{num_hops}\t\t{seq_num}")
            print()

    def visualize_network_graph(self):
        dot = Digraph()

        for node in self.routing_table:
            for destination, (next_hop, num_hops, seq_num) in self.routing_table[node].items():
                dot.node(node)
                dot.node(next_hop)
                dot.edge(node, next_hop, label=f"{destination}, {num_hops + 1}")

        dot.render('dsdv_graph', format='png', cleanup=True)
        print("DSDV Graph Visualization saved as 'dsdv_graph.png'")


# Example usage
dsdv = DSDV()
dsdv.update_routing_table('A', 'B', 'B', 0)
dsdv.update_routing_table('A', 'C', 'C', 0)
dsdv.update_routing_table('B', 'D', 'D', 1)
dsdv.update_routing_table('C', 'D', 'B', 2)

# Perform periodic update
dsdv.periodic_update()

# Display routing table of each node
dsdv.visualize_routing_table()

# Visualize the network graph
dsdv.visualize_network_graph()
