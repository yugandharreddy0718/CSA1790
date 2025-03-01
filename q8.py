graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
stack = ['A']
visited = set()

while stack:
    node = stack.pop()
    
    if node not in visited:
        print(node)  
        visited.add(node)  
        stack.extend(reversed(graph[node])) 

