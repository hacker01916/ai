'''Q1. Write a program to solve the 8-Puzzle Problem using the A* Search 
Algorithm'''

import heapq
class PuzzleState:
    def __init__(self, board, goal, moves=0, prev=None):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.prev = prev
        self.priority = self.moves + self.heuristic()
    def heuristic(self):
        distance = 0
        for i in range(1, 9):
            x1, y1 = divmod(self.board.index(i), 3)
            x2, y2 = divmod(self.goal.index(i), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
        return distance
    def get_neighbors(self):
        neighbors = []
        zero = self.board.index(0)
        x, y = divmod(zero, 3)
        directions = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for nx, ny in directions:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board[:]
                new_zero = nx*3 + ny
                new_board[zero], new_board[new_zero] = new_board[new_zero], new_board[zero]
                neighbors.append(PuzzleState(new_board, self.goal, self.moves+1, self))
        return neighbors
    def __lt__(self, other):
        return self.priority < other.priority
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, PuzzleState(start, goal))
    closed = set()
    while open_list:
        current = heapq.heappop(open_list)
        if current.board == goal:
            path = []
            while current:
                path.append(current.board)
                current = current.prev
            return path[::-1]
        closed.add(tuple(current.board))
        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in closed:
                heapq.heappush(open_list, neighbor)
    return None
start = [1,2,3,4,0,6,7,5,8]
goal  = [1,2,3,4,5,6,7,8,0]
solution = a_star(start, goal)
for step in solution:
    print(step)



'''Q2. Write a program to build a Convolutional Neural Network (CNN) for 
image recognition.(Orange vs Apple) '''

import tensorflow as tf
from tensorflow.keras import layers, models
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid') 
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'dataset/train', image_size=(64,64), batch_size=32)
test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'dataset/test', image_size=(64,64), batch_size=32)
model.fit(train_ds, epochs=10, validation_data=test_ds)
loss, acc = model.evaluate(test_ds)
print(f"Test Accuracy: {acc*100:.2f}%")



'''Q2 OR  Write a program to analyze the performance of a Support Vector Machine 
(SVM) on a classification dataset. '''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = SVC(kernel='linear') 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
