from collections import defaultdict


class Graph:
    """This class represents an directed graph using adjacency list representation"""
    def __init__(self, vertex):
        self.vert = vertex
        self.graph = defaultdict(list)
        self.time = 0

    # function to add an edge to graph
    def add_edge(self, next_vert, vert):
        self.graph[next_vert].append(vert)

    def scc_util(self, next_vert, low, disc_time, stack_member, store):
        """A recursive function that find finds and prints strongly connected components using DFS traversal

        :param next_vert: The vertex to be visited next
        :param low: earliest visited vertex that can be reached from subtree rooted with current vertex
        :param disc_time: discovery times of visited vertices
        :param stack_member: boolean check whether a node is in stack
        :param store: store all the connected ancestors
        """
        disc_time[next_vert] = self.time
        low[next_vert] = self.time
        self.time += 1
        stack_member[next_vert] = True
        store.append(next_vert)

        for v in self.graph[next_vert]:  # Go through all vertices adjacent to this
            if disc_time[v] == -1:  # If not visited, recursive call
                self.scc_util(v, low, disc_time, stack_member, store)
                low[next_vert] = min(low[next_vert], low[v])  # Check if the subtree has a connection ancestor of u
            elif stack_member[v]:  # Update low value of 'u' only if 'v' is still in stack
                low[next_vert] = min(low[next_vert], disc_time[v])

        # Head node found, pop the stack and print an SCC
        stack_vert = -1  # Store stack extracted vertices
        if low[next_vert] == disc_time[next_vert]:
            while stack_vert != next_vert:
                stack_vert = store.pop()
                print(stack_vert, end=" ")
                stack_member[stack_vert] = False
            print()  # Separate connections

    def dfs_traverse(self):
        """Perform DFS traversal"""
        # Mark all the vertices as not visited and initialize data structures
        disc_time = [-1] * self.vert
        low = [-1] * self.vert
        stack_member = [False] * self.vert
        store = []

        # Call the recursive helper function to find articulation points in DFS tree rooted with vertex 'i'
        for i in range(self.vert):
            if disc_time[i] == -1:
                self.scc_util(i, low, disc_time, stack_member, store)


if __name__ == "__main__":
    g1 = Graph(5)
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    print(g1.dfs_traverse())
