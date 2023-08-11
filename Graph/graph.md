# Code Challenge 36 : Graph Implementation 
## Description and Purpose:
The Graph class is designed to represent an undirected graph using an adjacency list data structure. The class provides methods to add vertices, add edges between vertices, retrieve the list of vertices, get the neighbors of a specific vertex, and get the total number of vertices in the graph.

### Approach:
The graph is represented using a dictionary, where each vertex is a key, and the value is a list of tuples representing connected vertices and their weights.
The add_vertex method simply adds a new vertex to the dictionary if it's not already present.
The add_edge method takes two vertices and an optional weight and adds an edge between them. It ensures that edges are not duplicated in the neighbors list.
The get_vertices method returns a list of all vertices in the graph.
The get_neighbors method returns the list of neighbors for a given vertex.
The size method returns the total number of vertices in the graph.
#### Efficiency:
Adding a vertex has an average time complexity of O(1), as it involves inserting a key into a dictionary.
Adding an edge has an average time complexity of O(1), as it involves appending to a list in a dictionary.
Retrieving the list of vertices has a time complexity of O(V), where V is the number of vertices.
Retrieving neighbors for a vertex has a time complexity of O(1), on average, as it directly retrieves the neighbors list from the dictionary.
Getting the size of the graph (number of vertices) has a time complexity of O(1).
Overall, the implementation is efficient for most graph operations, especially for retrieving neighbors and determining the graph's size.

[link to code ](graph.py)
