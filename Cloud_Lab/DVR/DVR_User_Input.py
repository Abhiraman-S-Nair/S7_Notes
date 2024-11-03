import copy

class Node:
    def __init__(self, name, all_nodes):
        self.name = name
        self.neighbors = {}  # Stores neighbors and their respective costs
        self.distance_vector = {node: float('inf') for node in all_nodes}  # Initialize all distances to infinity
        self.distance_vector[name] = 0  # Distance to itself is zero
        self.routing_table = {node: None for node in all_nodes}  # Routing table to store next hops

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost
        self.distance_vector[neighbor] = cost
        self.routing_table[neighbor] = neighbor  # Initial next hop is the neighbor itself

    def update_distance_vector(self, nodes):
        updated = False
        for dest in nodes:  # Iterate over all nodes in the network
            for neighbor, neighbor_cost in self.neighbors.items():
                if dest in nodes[neighbor].distance_vector:
                    new_cost = nodes[neighbor].distance_vector[dest] + neighbor_cost
                    if new_cost < self.distance_vector[dest]:
                        self.distance_vector[dest] = new_cost
                        self.routing_table[dest] = neighbor
                        updated = True
        return updated

def create_network():
    nodes = {}
    num_nodes = int(input("Enter the number of nodes: "))

    # Get all node names first
    all_nodes = []
    for _ in range(num_nodes):
        node_name = input("Enter node name: ")
        all_nodes.append(node_name)

    # Initialize nodes with all possible distances set to infinity
    for node_name in all_nodes:
        nodes[node_name] = Node(node_name, all_nodes)

    # Setup neighbors and initial distances
    for node_name in nodes:
        num_neighbors = int(input(f"\nEnter the number of neighbors for node {node_name}: "))
        for _ in range(num_neighbors):
            neighbor = input(f"Enter neighbor of {node_name}: ")
            cost = int(input(f"Enter cost to reach {neighbor} from {node_name}: "))
            nodes[node_name].add_neighbor(neighbor, cost)

    return nodes

def run_dvr_algorithm(nodes):
    print("\nStarting DVR algorithm...\n")
    stabilized = False
    while not stabilized:
        stabilized = True
        for node in nodes.values():
            if node.update_distance_vector(nodes):
                stabilized = False

def display_routing_tables(nodes):
    print("\nRouting tables after convergence:\n")
    for node_name, node in nodes.items():
        print(f"Node {node_name}:")
        for dest, next_hop in node.routing_table.items():
            if next_hop is not None:
                print(f"  To {dest} via {next_hop} with cost {node.distance_vector[dest]}")
            else:
                print(f"  To {dest} is unreachable")
        print()

if __name__ == "__main__":
    nodes = create_network()
    run_dvr_algorithm(nodes)
    display_routing_tables(nodes)
