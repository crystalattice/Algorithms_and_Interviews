import sys


class Graph:
    def __init__(self, vertices):
        self.verts = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_output(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.verts):
            print(f"Vertex {node} is {dist[node]} units away")

    def min_dist(self, dist, spt_set):
        """Find vertex w/ min dist value"""
        min_dist = sys.maxsize  # Initialize minimum distance for next node

        for v in range(self.verts):
            if dist[v] < min_dist and spt_set[v] is False:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        """Implement Dijkstra's algo"""
        dist = [sys.maxsize] * self.verts
        dist[src] = 0
        spt_set = [False] * self.verts

        for cout in range(self.verts):
            u = self.min_dist(dist, spt_set)  # Get min distance from vertices not processed

            spt_set[u] = True  # Add min dist vertex to SPT

            for v in range(self.verts):  # If current dist > new distance, update dist value of adj vertices
                if self.graph[u][v] > 0 and spt_set[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_output(dist)


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)
