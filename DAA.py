from collections import deque

# Read number of vertices and edges
n, m = map(int, input().split())

# Create adjacency list
graph = [[] for _ in range(n)]

# Read edges
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Sort neighbors in increasing order
for neighbors in graph:
    neighbors.sort()

# Read source and number of queries
s, q = map(int, input().split())

# Read target vertices
targets = []
for _ in range(q):
    targets.append(int(input()))

# -------------------------------
# Connected Components (Recursive DFS)
# -------------------------------
visited = [False] * n
labels = [-1] * n
component_count = 0

def dfs_component(vertex, label):
    visited[vertex] = True
    labels[vertex] = label

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_component(neighbor, label)

for vertex in range(n):
    if not visited[vertex]:
        component_count += 1
        dfs_component(vertex, vertex)

# -------------------------------
# DFS Traversal from Source
# -------------------------------
visited = [False] * n
dfs_order = []

def dfs(vertex):
    visited[vertex] = True
    dfs_order.append(vertex)

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(s)

# -------------------------------
# BFS Traversal from Source
# -------------------------------
visited = [False] * n
distance = [-1] * n
parent = [-1] * n
bfs_order = []

queue = deque()
queue.append(s)
visited[s] = True
distance[s] = 0

while queue:
    current = queue.popleft()
    bfs_order.append(current)

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            distance[neighbor] = distance[current] + 1
            parent[neighbor] = current
            queue.append(neighbor)

# -------------------------------
# Route Reconstruction
# -------------------------------
def get_route(target):
    if distance[target] == -1:
        return None

    path = []
    current = target

    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

# -------------------------------
# Output
# -------------------------------
print("COMPONENTS", component_count)
print("LABELS", *labels)
print("DFS", *dfs_order)
print("BFS", *bfs_order)

for target in targets:
    if distance[target] == -1:
        print("ROUTE", target, "UNREACHABLE")
    else:
        path = get_route(target)
        print("ROUTE", target, distance[target], *path)