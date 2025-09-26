# DFS (Iterative) Implementation in Python

def dfs_iterative(graph, start):
    visited = set()      # To track visited nodes
    stack = [start]      # Initialize stack with starting node

    while stack:
        node = stack.pop()    # Remove node from top of stack
        if node not in visited:
            print(node, end=" ")  # Process current node
            visited.add(node)     # Mark as visited
            stack.extend(reversed(graph[node]))  # Add neighbors to stack

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
print("DFS Iterative Traversal:")
dfs_iterative(graph, 'A')
