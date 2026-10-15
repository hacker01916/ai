#Q1

from queue import PriorityQueue
def a_star_search(graph, start, goal, heuristic):
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], start))
    g_cost = {start: 0}
    parent = {start: None}
    while not pq.empty():
        f, node = pq.get()
        print(f"Visiting: {node}")
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", g_cost[goal])
            return
        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                pq.put((f_cost, neighbor))
                parent[neighbor] = node
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 3)],
    'E': [('F', 2)],
    'F': []
}
heuristic = {'A': 6, 'B': 5, 'C': 3, 'D': 3, 'E': 2, 'F': 0}
print("A* Search from A to F:")
a_star_search(graph, 'A', 'F', heuristic)






#Q2

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
X = np.linspace(0, 10, 100)
Y = 2 * X + 3 + np.random.randn(100) * 0.5  
model = Sequential([
    Dense(1, input_dim=1, activation='linear')
])
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, Y, epochs=100, verbose=0)
Y_pred = model.predict(X)
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, Y_pred, color='red', label='Predicted Line')
plt.title('Linear Regression using ANN')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
