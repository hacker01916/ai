'''Q1 Write a program to implement the A* Search Algorithm to find the 
shortest path between a source node and a destination node. '''

from queue import PriorityQueue
def a_star(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((0, start))
    g = {node: float('inf') for node in graph}
    g[start] = 0
    parent = {start: None}
    while not pq.empty():
        _, current = pq.get()
        if current == goal:
            break
        for neighbor, cost in graph[current]:
            temp_g = g[current] + cost
            if temp_g < g[neighbor]:
                g[neighbor] = temp_g
                f = temp_g + h[neighbor]
                pq.put((f, neighbor))
                parent[neighbor] = current
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1], g[goal]
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3)],
    'C': [('D', 2)],
    'D': [('E', 5)],
    'E': []
}
h = {'A': 7, 'B': 6, 'C': 4, 'D': 2, 'E': 0}
path, cost = a_star(graph, 'A', 'E', h)
print("Shortest Path:", path)
print("Total Cost:", cost)



'''Q2) Write a program to implement the K-Means Clustering Algorithm for 
grouping data into clusters'''

import numpy as np
from sklearn.cluster import KMeans
X = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print("Cluster Centers:\n", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)
