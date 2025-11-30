from collections import deque

def bfs_distances(graph, start):
    """Returns the shortest path distances from start node to all other nodes."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

def compute_mostar_index(graph):
    """Computes the Mostar index of a graph given its adjacency list."""
    mostar_index = 0
    
    # Iterate over all edges (u, v) where u < v to avoid duplicates
    for u in graph:
        for v in graph[u]:
            if u < v:  # Ensure each edge is only considered once
                distances_from_u = bfs_distances(graph, u)
                distances_from_v = bfs_distances(graph, v)
                
                n_u = sum(1 for node in graph if distances_from_u[node] < distances_from_v[node])
                n_v = sum(1 for node in graph if distances_from_v[node] < distances_from_u[node])
                print(f"{u}, { v} {abs(n_u - n_v)}")
                mostar_index += abs(n_u - n_v)
    
    return mostar_index

# Read input
def read_graph():
    """Reads a graph from input as an adjacency list."""
    graph = {}
    n = int(input("Enter number of nodes: "))
    m = int(input("Enter number of edges: "))  # Add this line
    for _ in range(m):  # Loop over m edges, not n-1
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

if __name__ == "__main__":
    graph = read_graph()
    print("Mostar Index:", compute_mostar_index(graph))