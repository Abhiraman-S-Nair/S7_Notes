class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance_vector = {self: (0, self)}  # Distance to itself is zero, next hop is itself

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost
        self.distance_vector[neighbor] = (cost, neighbor)

    def update_distance_vector(self):
        updated = False
        for neighbor in self.neighbors:
            for dest, (dist, _) in neighbor.distance_vector.items():
                new_cost = self.neighbors[neighbor] + dist
                if dest not in self.distance_vector or self.distance_vector[dest][0] > new_cost:
                    self.distance_vector[dest] = (new_cost, neighbor)
                    updated = True
        return updated

    def __str__(self):
        routing_table = "\n".join(
            [
            f"Destination: {dest.name}, Distance: {dist}, Next Hop: {next_hop.name}"
            for dest, (dist, next_hop) in self.distance_vector.items()
            ]
        )
        return f"Router {self.name}, Routing Table:\n{routing_table}\n\n"

# Create routers
a = Router('A')
b = Router('B')
c = Router('C')
d = Router('D')

# Define neighbors and costs
a.add_neighbor(b, 1)
a.add_neighbor(c, 4)
b.add_neighbor(a, 1)
b.add_neighbor(c, 2)
b.add_neighbor(d, 6)
c.add_neighbor(a, 4)
c.add_neighbor(b, 2)
c.add_neighbor(d, 3)
d.add_neighbor(b, 6)
d.add_neighbor(c, 3)

# List of routers
routers = [a, b, c, d]

# Simulate the distance vector routing algorithm
iterations = 5
for i in range(iterations):
    print(f"Iteration {i+1}")
    updates = False
    for router in routers:
        if router.update_distance_vector():
            updates = True
        print(router)
    print()
    if not updates:
        break

# Final routing tables
print("Final Distance Vectors:")
for router in routers:
    print(router)
