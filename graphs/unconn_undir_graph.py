class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacent = [[] for node in range(vertex)]

    def dfs_util(self, temp, v, visited):
        visited[v] = True  # Mark the current vertex as visited
        temp.append(v)  # Store the vertex to list
        for i in self.adjacent[v]:  # Repeat for all vertices adjacent to this vertex v
            if not visited[i]:
                temp = self.dfs_util(temp, i, visited)  # Update the list
        return temp

    def add_edge(self, v, w):
        """Add edge between connected nodes"""
        self.adjacent[v].append(w)
        self.adjacent[w].append(v)

    def conn_nodes(self):
        """Get the connected nodes in undirected graph"""
        visited = []
        connections = []
        for i in range(self.vertex):
            visited.append(False)
        for v in range(self.vertex):
            if not visited[v]:
                temp = []
                connections.append(self.dfs_util(temp, v, visited))
        return connections


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    conns = g.conn_nodes()
    print("Below are the connected nodes:")
    for conn in conns:
        print(conn)
