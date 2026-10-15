#Q1
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
def dls(node, goal, depth):
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        for child in graph[node]:
            if dls(child, goal, depth - 1):
                return True
    return False
def ids(start, goal, max_depth):
    for depth in range(max_depth):
        print(f"Searching at depth {depth}...")
        if dls(start, goal, depth):
            print(f"Goal {goal} found at depth {depth}")
            return
    print("Goal not found within depth limit.")
ids('A', 'E', 4)



#Q2
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X = [[1.8, 6.2], [1.6, 5.8], [3.0, 7.0], [3.2, 7.5]]
y = ['short', 'short', 'tall', 'tall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

