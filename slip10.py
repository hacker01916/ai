#Q1
def means_end_analysis(current, goal):
    print("Current State:", current)
    print("Goal State:", goal)
    while current != goal:
        if current < goal:
            current += 1
            print("Action: Increase value")
        elif current > goal:
            current -= 1
            print("Action: Decrease value")
        print("New State:", current)
    print("Goal Achieved!")
means_end_analysis(2, 5)

#Q2

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = {
    'Study_Hours': [2, 3, 4, 5, 6, 7, 1, 2, 5, 8],
    'Attendance': [60, 65, 70, 75, 80, 85, 55, 62, 78, 90],
    'Assignment_Score': [55, 60, 65, 70, 75, 80, 50, 58, 72, 85],
    'Result': ['Fail', 'Fail', 'Fail', 'Pass', 'Pass',
               'Pass', 'Fail', 'Fail', 'Pass', 'Pass']
}
df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance', 'Assignment_Score']]
y = df['Result']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Actual Result:", list(y_test))
print("Predicted Result:", list(y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
new_student = pd.DataFrame(
    [[6, 80, 75]],
    columns=['Study_Hours', 'Attendance', 'Assignment_Score']
)
print("New Student Result:", model.predict(new_student)[0])
