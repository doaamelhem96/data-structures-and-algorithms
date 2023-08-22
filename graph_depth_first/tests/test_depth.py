import pytest
from depth import *

# Create a fixture for the graph
@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B", weight=3)
    graph.add_edge("A", "C", weight=2)
    graph.add_edge("B", "D", weight=4)
    graph.add_edge("C", "D", weight=1)

    return graph


def test_depth_first_traversal(sample_graph):
    start_node = "A"
    result = sample_graph.depth_first(start_node)
    assert result == ["A", "B", "D", "C"] 

def test_depth_first_empty_graph():
    graph = Graph()

    graph.add_vertex("A")
    start_node = "A"  
    result = graph.depth_first(start_node)
    assert result == [start_node] 


def test_depth_first_invalid_start_node(sample_graph):
    with pytest.raises(ValueError):
        start_node = "E"  
        sample_graph.depth_first(start_node)