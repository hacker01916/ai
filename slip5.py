#Q1
def dls(graph, start, goal, limit):
    def recursive_dls(node, goal, limit, path):
        if node == goal:
            return path
        if limit <= 0:
            return None
        for neighbor in graph.get(node, []):
            result = recursive_dls(neighbor, goal, limit - 1, path + [neighbor])
            if result:
                return result
        return None
    return recursive_dls(start, goal, limit, [start])
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
goal = 'E'
limit = 2
print("Path found:", dls(graph, 'A', goal, limit))




##Q2

from sklearn.datasets import make_classification
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
X, y = make_classification(n_samples=300, n_features=2, n_informative=2,
                           n_redundant=0, n_classes=2, random_state=42)
model = BernoulliNB()
model.fit(X, y)
X_test = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_true = [0, 1, 0, 1]
y_pred = model.predict(X_test)
acc = accuracy_score(y_true, y_pred)
print("Predicted:", y_pred)
print("Accuracy Score:", acc)


#Q2(OR)
from sklearn import svm
X = [
    [5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.1, 1.5, 0.2], [5.0, 3.6, 1.4, 0.2], [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5], [6.9, 3.1, 4.9, 1.5], [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9]
]
y = [0, 0, 0, 0, 1, 1, 2, 2, 2, 2]
X_test = [
    [5.2, 3.4, 1.5, 0.2],
    [6.5, 3.0, 4.6, 1.5],
    [6.2, 3.0, 5.2, 2.0]
]
model = svm.SVC(kernel='linear')
model.fit(X, y)
y_pred = model.predict(X_test)
print("Predicted Classes:", y_pred)
