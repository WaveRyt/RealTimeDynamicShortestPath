import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from graph import Graph
from dynamic_dijkstra import DynamicShortestPath

def test_simple_shortest_path():
    g = Graph()
    g.add_edge(1,2,5)
    g.add_edge(2,3,3)
    dsp = DynamicShortestPath(g)
    path, dist = dsp.shortest_path(1,3)
    assert path == [1,2,3]
    assert dist == 8

def test_update_changes_path():
    g = Graph()
    g.add_edge(1,2,10)
    g.add_edge(2,3,1)
    g.add_edge(1,3,50)
    dsp = DynamicShortestPath(g)
    p, d = dsp.shortest_path(1,3)
    assert d == 11
    g.update_edge(1,2,1)
    dsp.notify_edge_changed()
    p2, d2 = dsp.shortest_path(1,3)
    assert d2 == 2