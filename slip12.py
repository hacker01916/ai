#Q1
from collections import deque
def bfs(start, goal, graph):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
graph = {
    'Monkey': ['MoveToChair', 'MoveToBanana'],
    'MoveToChair': ['ClimbChair'],
    'ClimbChair': ['GrabBanana'],
    'MoveToBanana': ['GrabBanana'],
    'GrabBanana': []
}
solution = bfs('Monkey', 'GrabBanana', graph)
print("Path to reach banana:", solution)



##Q(2(OR))
import tensorflow as tf
import numpy as np
X = np.array([1,2,3,4,5,6,7,8], dtype=float)
Y = np.array([2,4,6,8,10,12,14,16], dtype=float)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(X, Y, epochs=100, verbose=0)
print("Prediction for 9:", model.predict([9])[0][0])


