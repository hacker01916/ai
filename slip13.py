#Q1
from collections import deque
def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == target or b == target:
            print("Target reached!")
            return
        states = [
            (jug1, b),
            (a, jug2),
            (0, b),
            (a, 0), 
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),
            (a + min(b, jug1 - a), b - min(b, jug1 - a)) 
        ]
        for state in states:
            if state not in visited:
                queue.append(state)
water_jug_bfs(4, 3, 2)


#Q2(OR)
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_edges_from([
    ("Rahul", "Student", {"relation": "is a"}),
    ("Rahul", "Pune", {"relation": "lives in"}),
    ("Rahul", "Python", {"relation": "learns"}),
    ("Python", "Programming", {"relation": "is a"}),
    ("Pune", "Maharashtra", {"relation": "located in"})
])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue",
        node_size=2500, arrows=True)
labels = nx.get_edge_attributes(G, "relation")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Simple Knowledge Graph")
plt.show()
print("Knowledge Graph created successfully!")
