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





    def depth_first(self, start_node):
        if start_node not in self.vertices:
            raise ValueError(f"Start node '{start_node}' not found in the graph.")

        visited = set()
        result = []

        def dfs_helper(node):
            visited.add(node)
            result.append(node)

            neighbors = self.get_neighbors(node)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_node)
        return result