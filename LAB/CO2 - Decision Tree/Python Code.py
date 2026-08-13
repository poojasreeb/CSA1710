# Decision Tree Classification

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset
# [Study Hours, Attendance]
X = [
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 70],
    [6, 75],
    [7, 80],
    [8, 85],
    [9, 90],
    [10, 95]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Display results
print("Actual Values   :", y_test)
print("Predicted Values:", y_pred)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy * 100, "%")

# Predict a new student
new_student = [[6, 78]]
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("New Student: Pass")
else:
    print("New Student: Fail")
