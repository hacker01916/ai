#Q1

from collections import deque
def water_jug(cap1, cap2, target):
    q = deque([(0, 0)])
    visited = set()
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            print("Target reached!")
            return
        q.append((cap1, y)) 
        q.append((x, cap2)) 
        q.append((0, y))    
        q.append((x, 0))   
        p = min(x, cap2 - y)
        q.append((x - p, y + p))
        p = min(y, cap1 - x)
        q.append((x + p, y - p))
water_jug(4, 3, 2)




##Q2)
def is_safe(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True
def solve_csp(graph, colors, node, m):
    if node == len(graph):
        return True
    for color in range(1, m + 1):
        if is_safe(graph, colors, node, color):
            colors[node] = color

            if solve_csp(graph, colors, node + 1, m):
                return True
            colors[node] = 0  
    return False
graph = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}
colors = [0] * 5
m = 5
if solve_csp(graph, colors, 0, m):
    print("Solution found:")
    for i in range(5):
        print("Vertex", i + 1, ":", "Color", colors[i])
else:
    print("No solution exists")

    
    
 ##Q2(OR)
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def display(self, level=0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 2)
root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
print("Game Tree:")
root.display()
  