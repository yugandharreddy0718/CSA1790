from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

queue = deque(['A'])
visited = set()


while queue:
    node = queue.popleft()
    if node not in visited:
        print(node)  
        visited.add(node)
        queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
