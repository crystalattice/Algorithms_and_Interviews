from collections import defaultdict


class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)  # Dictionary of adjacency List
		self.verts = vertices  # Number of vertices

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def recursive_topo_sort(self, v, visited, stack):
		"""Recursively find all the vertices adjacent to this vertex"""
		visited[v] = True  # Mark the current node as visited.
		for i in self.graph[v]:
			if not visited[i]:
				self.recursive_topo_sort(i, visited, stack)
		stack.insert(0, v)  # Push current vertex to stack

	def topo_sort(self):
		"""Perform the topological sort.

		Uses the recursive method to find adjacent vertices
		"""
		visited = [False] * self.verts  # Mark all the vertices as not visited
		stack = []

		for i in range(self.verts):  # Call recursive method
			if not visited[i]:
				self.recursive_topo_sort(i, visited, stack)
		print(stack)


if __name__ == "__main__":
	g = Graph(6)
	g.add_edge(5, 2)
	g.add_edge(5, 0)
	g.add_edge(4, 0)
	g.add_edge(4, 1)
	g.add_edge(2, 3)
	g.add_edge(3, 1)

	print("Topological Sort of the given graph")
	print(g.topo_sort())
