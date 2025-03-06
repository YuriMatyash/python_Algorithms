from data_structures.linkedList import LinkedList

class Graph:
    # Constructor
    def __init__(self, vertices, edges):
        self.vertices = {}

        for vertex in vertices:
            self.vertices[vertex] = LinkedList(vertex)


        for edge in edges:
            v1, v2 = edge
            if v1 in self.vertices:
                self.vertices[v1].add(v2)
            if v2 in self.vertices:
                self.vertices[v2].add(v1)

    # Check if vertex exists in graph
    def is_vertex(self, vertex):
        if vertex not in self.vertices:
            return False
        return True

    # Check if edge exists in graph
    def is_edge(self, edge):
        v1, v2 = edge

        if v1 not in self.vertices:
            return False
        
        return self.vertices[v1].is_node(v2)
        
    # Remove edge from graph
    def remove_edge(self, edge):
        if not self.is_edge(edge):
            return
        
        v1, v2 = edge
        self.vertices[v1].remove(v2)
        self.vertices[v2].remove(v1)
    
    # Removes vertex from graph
    def remove_vertex(self, vertex):
        if not self.is_vertex(vertex):
            return
        
        for h in self.vertices:
            self.vertices[h].remove(vertex)
        
        del self.vertices[vertex]
    
    # Adds new vertex
    def add_vertex(self, vertex):
        if vertex in self.vertices:
            return
        
        self.vertices[vertex] = LinkedList(vertex)

    # Adds new edge
    def add_edge(self, edge):
        if self.is_edge(edge):
            return

        v1,v2 = edge
        if v1 not in self.vertices or v2 not in self.vertices:
            return

        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    # Prints the graph
    def print_graph(self):
        for vertex, linked_list in self.vertices.items():
            print(f'{vertex} -> ', end='')
            linked_list.printList()
            

        
        





        

        


