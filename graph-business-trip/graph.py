class Graph:
    def __init__(self):
        self.vertices = {}  # Using a dictionary to store vertices and their neighbors
    
    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []
        return value
    
    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # Check if the edge already exists before adding it
            if (vertex2, weight) not in self.vertices[vertex1]:
                self.vertices[vertex1].append((vertex2, weight))
            if (vertex1, weight) not in self.vertices[vertex2]:
                self.vertices[vertex2].append((vertex1, weight))  # Assuming an undirected graph
    
    def get_vertices(self):
        return list(self.vertices.keys())
    
    
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        return []
    
    def size(self):
        return len(self.vertices)


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

print("Vertices:", graph.get_vertices())
print("Neighbors of A:", graph.get_neighbors("A"))
print("Graph size:", graph.size())
