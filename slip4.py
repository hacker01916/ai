#Q1

from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

print("BFS Traversal starting from A:")
bfs(graph, 'A')


#Q2

def is_even(x):
    return x % 2 == 0
def forall(domain, predicate):
    return all(predicate(x) for x in domain)
def exists(domain, predicate):
    return any(predicate(x) for x in domain)
numbers = [1, 2, 3, 4, 5, 6]
print("All numbers are even:", forall(numbers, is_even))
print("There exists an even number:", exists(numbers, is_even))



##Q2(OR)
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
X, y = make_blobs(n_samples=200, centers=3, n_features=2, cluster_std=1.5, random_state=42)
model = GaussianNB()
model.fit(X, y)
test_values = [[-2, 5], [0, 0], [6, -0.3]]
true_output = [0, 1, 1]
predicted = model.predict(test_values)
acc = accuracy_score(true_output, predicted)
print("Predicted:", predicted)
print("Accuracy Score:", acc)
