class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.routing_table = {}

    def update_routing_table(self, destination, next_node, distance, sequence_number):
        """
        Update or add an entry in the routing table
        """
        if destination in self.routing_table:
            # Update existing entry if necessary
            if sequence_number is not None and (
                    self.routing_table[destination]['sequence_number'] is None or sequence_number > self.routing_table[
                destination]['sequence_number']):
                self.routing_table[destination] = {'next_node': next_node,
                                                   'distance': distance,
                                                   'sequence_number': sequence_number}
        else:
            # Add new entry to the routing table
            self.routing_table[destination] = {'next_node': next_node,
                                               'distance': distance,
                                               'sequence_number': sequence_number}

    def print_routing_table(self):
        """
        Print the routing table
        """
        print(f"Sample Routing Table for Node {self.node_id}")
        print("Dest.\tNxt Node\tDist.\tSeq.no.")
        for destination, values in self.routing_table.items():
            print(f"{destination}\t{values['next_node']}\t\t{values['distance']}\t{values['sequence_number']}")


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        """
        Add a new node to the graph
        """
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, node_id1, node_id2, distance):
        """
        Add an edge between two nodes with given distance
        """
        self.nodes[node_id1].update_routing_table(node_id2, node_id2, distance, 0)
        self.nodes[node_id2].update_routing_table(node_id1, node_id1, distance, 0)

    def delete_node(self, deleted_node_id):
        """
        Delete a node from the network and update routing tables accordingly
        """
        for node_id, node in self.nodes.items():
            if node_id != deleted_node_id:
                node.update_routing_table(deleted_node_id, None, float('inf'), None)
                for destination, values in node.routing_table.items():
                    if values['next_node'] == deleted_node_id:
                        node.update_routing_table(destination, None, values['distance'], values['sequence_number'])

    def add_back_node(self, node_id, new_sequence_number):
        """
        Add a previously deleted node back to the network with an increased sequence number
        """
        for source_node_id, source_node in self.nodes.items():
            if source_node_id != node_id:
                for destination, values in source_node.routing_table.items():
                    if values['next_node'] is None:
                        source_node.update_routing_table(destination, node_id, values['distance'], new_sequence_number)

    def print_graph_routing_tables(self):
        """
        Print routing tables for all nodes in the graph
        """
        for node_id, node in self.nodes.items():
            node.print_routing_table()
            print()


# Sample usage:
if __name__ == "__main__":
    graph = Graph()

    # Add nodes to the graph
    for node_id in ['N1', 'N2', 'N3', 'N4']:
        graph.add_node(node_id)

    # Add edges to the graph
    graph.add_edge('N1', 'N2', 1)
    graph.add_edge('N2', 'N3', 1)
    graph.add_edge('N2', 'N4', 2)

    # Print routing tables before deletion
    print("BEFORE DELETION OF N4")
    graph.print_graph_routing_tables()

    # Delete node N4 from the graph
    deleted_node_id = 'N4'
    graph.delete_node(deleted_node_id)

    # Print routing tables after deletion - (BROADCASTING NEW DISTANCE OF N4 TO ALL NODES)
    print("\nAFTER DELETION OF N4")
    graph.print_graph_routing_tables()

    # Add back node N4 with increased sequence number
    new_sequence_number = 30
    graph.add_back_node(deleted_node_id, new_sequence_number)

    # Print routing tables after adding back
    print("\nAFTER ADDING OF N4 AGAIN TO GRAPH TO SAME LOCATION")
    graph.print_graph_routing_tables()
