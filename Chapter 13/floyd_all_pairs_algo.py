import math

# Constants
VERTS = 4
INF = math.inf  # This value will be used for vertices not connected to each other


def floyd_warshall(graph_matrix):
    """Initializing the solution matrix with same data as input graph matrix"""
    dist = [[j for j in i] for i in graph_matrix]  # Output matrix

    for k in range(VERTS):  # Add all vertices one by one to the set of intermediate vertices.
        for i in range(VERTS):  # Select all vertices as source, one by one
            for j in range(VERTS):  # Pick all vertices as destination for the above picked source
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # If k is on the shortest path, update the dist
    print_output(dist)


def print_output(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    print("Vert 0\tVert1\tVert2\tVert3")
    for i in range(VERTS):
        for j in range(VERTS):
            if dist[i][j] == INF:
                print("INF\t", end="")
            else:
                print(f"{dist[i][j]}\t", end="")

            if j == VERTS - 1:
                print("")


if __name__ == "__main__":
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    floyd_warshall(graph)
