class Graph:
    
    def __init__(self, V):
        # array
        self.vertices = [None] * len(V)
        for i in range(len(V)):
            self.vertices[i] = [None] * len(V)

        """
        # matrix
        self.matrix = [None] * len(V)
        for i in range(V):
            self.matrix[i] = [None] * len(V)
        """

    def add_edges(self, argv_edges):
        for edge in argv_edges:
            u, v, w = edge[0], edge[1], edge[2]
            self.vertices[u].add_edge(Edge(u, v, w))

    def bfs(self, source):
        """
        Function for BFS, starting from source
        Very Very Basic
        """
        return_bfs = []
        discovered = []
        discovered.append(source)
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True
        return return_bfs

    def dfs(self, source):
        """
        Function for DFS, starting from source
        Very Very Basic
        """
        return_dfs = []
        discovered = []
        discovered.append(source)
        while len(discovered) > 0:
            u = discovered.pop()
            u.visited = True
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True
        return return_dfs

    def dfs_recursion(self, current_vertex):
        """
        Function for DFS, starting from source
        Recursion
        """
        current_vertex.visited = True
        for next_vertex in current_vertex.adjacent:
            if next_vertex.visited == False:
                self.dfs_recursion(next_vertex)

    def bfs_distance(self, source):
        """
        Function for BFS, starting from source
        Very Very Basic
        """
        discovered = []
        discovered.append(source)
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            if u == destination:
                return
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True
                    v.distance = u.distance + 1
                    v.previous = u
        # backtracking

    def dijkstra(self, source):
        """
        Function for Dijkstra, starting from source
        Very Very Basic
        """
        discovered = Heap()
        discovered.append(source.distance, source)            # append(key, data)
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            # Perform edge relaxation on all adjacent vertices
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:                      # means distance is still inf
                    discovered.append(v)                       # means I have discovered v, adding it to queue
                    v.discovered = True
                    v.distance = u.distance + edge.w
                    v.previous = u
                    discovered.append(v.distance, v)
                # It is in heap, but not yet finalise
                else if v.visited == False:
                    # If i find a shorter route, change it
                    if v.distance > u.distance:
                        # Update Distance
                        v.distance = u.distance + edge.w
                        # Update Heap

                        discovered.update(v, distance)          # update vertex v in heap, with distance v.distance (smaller); perform heap


    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex" + str(vertex) + "\n"
        return return_string

class Vertex:
    
    def __init(self):
        self.id = id
        # list
        self.edges = []
        # For Traversal
        self.discovered = False
        self.visited = True
        # Distance
        self.distance = 0

    def add_edge(self, edge):
        self.edges.append(edge)

    def added_to_queue(self):
        self.discovered = True

    def visited_node(self):
        self.visited = True

    def __str__(self):
        return_string = str(self.id)
        return return_string

class Edge:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

if __name__ == "__main__":
    vertices = [0,1,2,3,4]
    my_graph = Graph(V=vertices)