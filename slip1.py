#Q1

from collections import deque
initial = ("door", "window", False, False)
goal = True
def get_next_states(state):
    monkey, box, on_box, banana = state
    states = []
    if not on_box:
        for pos in ["door", "window", "center"]:
            if pos != monkey:
                states.append(
                    ((pos, box, False, banana),
                     "Monkey walks from " + monkey + " to " + pos)
                )
    if not on_box and monkey == box and box == "window":
        states.append(
            (("center", "center", False, banana),
             "Monkey pushes box from window to center")
        )
    if not on_box and monkey == box:
        states.append(
            ((monkey, box, True, banana),
             "Monkey climbs onto the box")
        )
    if on_box and monkey == "center" and box == "center":
        states.append(
            (("center", "center", True, True),
             "Monkey gets the banana")
        )
    return states
def bfs():
    queue = deque()
    queue.append((initial, []))
    visited = set()
    visited.add(initial)
    while queue:
        state, path = queue.popleft()
        if state[3] == goal:
            return path
        for next_state, action in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
    return None
solution = bfs()
print("Solution using BFS:")
for i, action in enumerate(solution, 1):
    print(i, ".", action)
    
    
##Q2

import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}
def a_star(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path, g
        if current in visited:
            continue
        visited.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )
    return None, float('inf')
path, cost = a_star('A', 'G')
print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)


#Q2(OR)
colors = ["Red", "Green", "Blue"]
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
color = {}
def is_safe(region, selected_color):
    for neighbor in graph[region]:
        if neighbor in color and color[neighbor] == selected_color:
            return False
    return True
def map_coloring(regions, index):
    if index == len(regions):
        return True
    region = regions[index]
    for selected_color in colors:
        if is_safe(region, selected_color):
            color[region] = selected_color
            if map_coloring(regions, index + 1):
                return True
            del color[region]
    return False
regions = ['A', 'B', 'C', 'D']
if map_coloring(regions, 0):
    print("Map Coloring Solution:")
    for region in regions:
        print(region, ":", color[region])
else:
    print("No solution exists")
