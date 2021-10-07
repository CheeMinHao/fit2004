class Graph:
    def __init__(self, V):
        # Initialise Adjacency List
        self.vertices = [None] * V
        # Fill the List with the Vertex and its weights
        for i in range(V):
            self.vertices[i] = Vertex(i)

    def add_edges(self, argv_edges):
        for edge in argv_edges:
            u, v, w = edge[0], edge[1], edge[2]
            self.vertices[u].add_edge(Edge(u, v, w))

    def __str__(self):
        # Output Graph content for readability
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + "\n"
        return return_string

class Vertex:
    def __init__(self, id):
        # Initialise edges to contain the vertex
        self.id = id
        self.edges = []

    def add_edge(self, edge):
        # Append edge related to vertex
        self.edges.append(edge)

    def __str__(self):
        # Output Vertex ID for readability
        return_string = str(self.id)
        for edge in self.edges:
            return_string = return_string + "\n with edges " + str(edge)
        return return_string

class Edge:
    def __init__(self, u, v, w):
        # initialise edges
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        # Output Edge for readability
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string
        

if __name__ == "__main__":
    # Creating sample graph to show output
    total_vertices = 5
    my_graph = Graph(total_vertices)
    
    # Append the edges and insert into graph
    edges = []
    edges.append((3,1,5))
    edges.append((1,2,1))
    edges.append((3,2,-5))

    my_graph.add_edges(edges)
    print(my_graph)