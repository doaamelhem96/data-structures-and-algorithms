import pytest
from graph import Graph

@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", weight=2)
    return graph

def test_add_vertex(sample_graph):
    assert "A" in sample_graph.get_vertices()
    assert "B" in sample_graph.get_vertices()

def test_add_edge(sample_graph):
    neighbors_a = sample_graph.get_neighbors("A")
    neighbors_b = sample_graph.get_neighbors("B")

    assert ("B", 2) in neighbors_a
    assert ("A", 2) in neighbors_b

def test_get_vertices(sample_graph):
    vertices = sample_graph.get_vertices()
    assert len(vertices) == 2
    assert "A" in vertices
    assert "B" in vertices

def test_get_neighbors(sample_graph):
    neighbors_a = sample_graph.get_neighbors("A")
    neighbors_b = sample_graph.get_neighbors("B")

    assert len(neighbors_a) == 1
    assert len(neighbors_b) == 1

    assert ("B", 2) in neighbors_a
    assert ("A", 2) in neighbors_b

def test_size(sample_graph):
    assert sample_graph.size() == 2

def test_single_vertex_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_edge("A", "A", weight=1)

    assert graph.size() == 1
    neighbors_a = graph.get_neighbors("A")
    assert len(neighbors_a) == 1
    assert neighbors_a[0] == ("A", 1)
