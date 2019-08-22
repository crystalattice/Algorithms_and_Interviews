class Graph:
    def __init__(self, vertices):
        self.verts = vertices  # No. of vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        """Find the set of an element"""
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """Union, by rank, of two sets"""
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        # Union by rank
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:  # If ranks are same, then make one as root and increment its rank by one
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_algo(self):
        """Find the MST

        V is the number of vertices in graph
        """
        result = []  # Store MST
        i = 0  # Sorted edges
        e = 0  # Used for result[]
        parent = []
        rank = []

        # Sort all the edges in non-decreasing order of their weight.
        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.verts):  # Create V subsets with single elements
            parent.append(node)
            rank.append(0)

        while e < self.verts - 1:  # Number of edges to be taken is equal to V-1
            u, v, w = self.graph[i]  # Extract edge components from graph
            i = i + 1

            # Find smallest edge
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:  # Check if including this edge doesn't cause cycle
                e = e + 1
                result.append([u, v, w])  # Include edge in result
                self.union(parent, rank, x, y)
            # Else discard the edge

        print("The following are the edges in the MST")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_algo()
