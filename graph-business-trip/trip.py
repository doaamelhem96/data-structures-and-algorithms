from graph import *
def business_trip(graph, cities):
    total_cost = 0

    for i in range(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        neighbors = graph.get_neighbors(current_city)
        direct_flight = False

        for neighbor, weight in neighbors:
            if neighbor == next_city:
                total_cost += weight
                direct_flight = True
                break

        if not direct_flight:
            return None

    return total_cost

# Example usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B", weight=3)
graph.add_edge("A", "C", weight=2)
graph.add_edge("B", "D", weight=4)
graph.add_edge("C", "D", weight=1)

cities = ["A", "B", "D"]
print("Total cost:", business_trip(graph, cities))  # Output: Total cost: 7
