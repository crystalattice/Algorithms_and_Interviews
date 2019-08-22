from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Dictionary of adjacency List
        self.verts = vertices  # Number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topo_sort(self):
        in_degree = [0] * self.verts  # List to store in-degrees of all vertices
        visited_verts = 0  # Initialize count of visited vertices
        top_order = []  # List of topo sorted vertices
        queue = []  # List of vertices with 0 in-degrees

        for i in self.graph:  # Traverse adjacency lists to fill in-degrees of vertices.
            for j in self.graph[i]:
                in_degree[j] += 1

        for i in range(self.verts):   # Enqueue all in-degree = 0 vertices
            if in_degree[i] == 0:
                queue.append(i)

        while queue:  # Dequeue vertices from queue and enqueue adjacent vertex if adjacent in-degree = 0
            u = queue.pop(0)
            top_order.append(u)
            for i in self.graph[u]:  # Iterate through all neighbouring nodes decrease their in-degree by 1
                in_degree[i] -= 1
                if in_degree[i] == 0:  # If in-degree becomes zero, add it to queue
                    queue.append(i)
            visited_verts += 1

        try:
            if visited_verts != self.verts:  # Check if there was a cycle
                raise ValueError
            else:
                print(top_order)
        except ValueError:
            print("There exists a cycle in the graph")


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(0, 5)

    print("Topological Sort of the given graph")
    print(g.topo_sort())
