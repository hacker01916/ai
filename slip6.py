#Q1
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D'],
    'F': ['C']
}
print("DFS Traversal starting from A:")
dfs(graph, 'A')

#Q2
from sklearn import svm
X = [[1, 2], [2, 3], [5, 5]]
y = [0, 0, 1]
model = svm.SVC(kernel='rbf', gamma='scale')
model.fit(X, y)
test_input = [[4, 4]]
prediction = model.predict(test_input)
print("Predicted class for [4,4]:", prediction[0])


#Q2(OR)
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
inputs = np.array([
    [3, 1.5], [2, 1], [4, 1.5], [3, 4],
    [3.5, 0.5], [2, 0.5], [5.5, 1], [1, 1]
])
targets = np.array([[0], [1], [0], [1], [0], [1], [1], [0]])
np.random.seed(42)
weights = np.random.rand(2, 1)
learning_rate = 0.1
epochs = 20
for epoch in range(epochs):
    input_layer = inputs
    outputs = sigmoid(np.dot(input_layer, weights))
    error = targets - outputs
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments) * learning_rate
print("Final weights:\n", weights)
print("Predicted outputs:\n", outputs)
