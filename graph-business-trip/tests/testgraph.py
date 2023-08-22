import pytest
from trip import *

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

# Test cases for business_trip function
def test_business_trip_direct_route(sample_graph):
    cities = ["A", "B", "D"]
    assert business_trip(sample_graph, cities) == 7

def test_business_trip_indirect_route(sample_graph):
    cities = ["A", "C", "D"]
    assert business_trip(sample_graph, cities) == 3

def test_business_trip_no_route(sample_graph):
    cities = ["A", "D"]
    assert business_trip(sample_graph, cities) is None

def test_business_trip_invalid_city(sample_graph):
    cities = ["A", "E"]
    assert business_trip(sample_graph, cities) is None

def test_business_trip_empty_route(sample_graph):
    cities = []
    assert business_trip(sample_graph, cities) == 0

if __name__ == "__main__":
    pytest.main()
