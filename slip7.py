#Q1
from queue import PriorityQueue
def a_star(graph, heuristics, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {start: None}
    while not pq.empty():
        _, current = pq.get()
        if current == goal:
            break
        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost
            if temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + heuristics[neighbor]
                pq.put((f_cost, neighbor))
                parent[neighbor] = current
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path, g_cost[goal]
graph = {
    'V1': [('V2', 2), ('V3', 4)],
    'V2': [('V4', 3)],
    'V3': [('V4', 1), ('V5', 5)],
    'V4': [('V6', 2)],
    'V5': [('V6', 1)],
    'V6': []
}
heuristics = {'V1': 7, 'V2': 6, 'V3': 5, 'V4': 2, 'V5': 1, 'V6': 0}
path, cost = a_star(graph, heuristics, 'V1', 'V6')
print("Shortest Path:", path)
print("Total Cost:", cost)


#Q2
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}
def is_valid(node, color, assignment):
    for neighbor in neighbors[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def csp_coloring(assignment):
    if len(assignment) == len(neighbors):
        return assignment
    node = [n for n in neighbors if n not in assignment][0]
    for color in colors:
        if is_valid(node, color, assignment):
            assignment[node] = color
            result = csp_coloring(assignment)
            if result:
                return result
            assignment.pop(node)
    return None
solution = csp_coloring({})
print("Coloring Solution:", solution)


