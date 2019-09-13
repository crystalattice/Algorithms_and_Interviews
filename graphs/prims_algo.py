import sys


class Graph:
    def __init__(self, vertices):
        self.verts = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]  # Create a matrix of vertices

    def print_mst(self, parent):
        """Print MST construct in parent array"""
        print("Edge Weight")
        for i in range(1, self.verts):
            print(f"{parent[i]}-{i} {self.graph[i][parent[i]]}")

    def min_key(self, key, mst_set):
        """Find vertex w/ minimum distance value.

        Uses the set of vertices not yet included in shortest path tree
        """
        min_dist = sys.maxsize  # Maximum int size
        min_index = 0

        for v in range(self.verts):
            if key[v] < min_dist and mst_set[v] is False:
                min_dist = key[v]
                min_index = v

        return min_index

    def mst_func(self):
        """Create MST for graph"""
        key = [sys.maxsize] * self.verts  # Key values used to pick minimum weight edge in cut
        parent = [None] * self.verts  # Store constructed MST
        key[0] = 0  # Create first vertex
        mst_set = [False] * self.verts

        parent[0] = -1  # First node is always the root

        for cout in range(self.verts):
            u = self.min_key(key, mst_set)  # Pick the minimum distance vertex from vertices not yet processed.
            mst_set[u] = True  # Put the min distance vertex in the shortest path tree

            for v in range(self.verts):  # Update dist value of the adj verts if the dist is greater than new distance
                if 0 < self.graph[u][v] < key[v] and mst_set[v] is False:  # Update the key only if graph[u][v] is
                    # smaller than key[v]
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


if __name__ == "__main__":
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.mst_func()
