# BFS Implementation in Python
from collections import deque

def bfs(graph, start):
    visited = set()            # To track visited nodes
    queue = deque([start])     # Initialize queue with starting node

    while queue:
        node = queue.popleft()  # Remove node from front of queue
        if node not in visited:
            print(node, end=" ")  # Process current node
            visited.add(node)     # Mark as visited
            queue.extend(graph[node])  # Add neighbors to queue

# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Driver code
print("BFS Traversal:")
bfs(graph, 'A')
