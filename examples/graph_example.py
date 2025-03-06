from data_structures.graph import Graph

def test_graph():
    V = [1,2,3,4]
    E = [(1,2),(1,3),(1,4),(2,3),(2,4)]

    G = Graph(V,E)
    G.print_graph()
    print(f'There are: {G.count_vertex()} Vertecies and {G.count_edge()} edges!')
    print(f'1 is a vertex! {G.is_vertex(1)}\n5 is a vertex! {G.is_vertex(5)}')
    print(f'(1,3) is an edge! {G.is_edge((1,3))}\n(3,4) is an edge! {G.is_vertex((3,4))}')

    print("\nLet's make a line!\n")
    G.remove_vertex(4)
    G.remove_edge((1,3))
    G.remove_edge((1,4))
    G.remove_edge((2,4))
    G.add_vertex(0)
    G.add_edge((0,1))
    G.print_graph()
    print(f'There are: {G.count_vertex()} Vertecies and {G.count_edge()} edges!')

if __name__ == "__main__":
    test_graph()