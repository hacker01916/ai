#Q1

import random
def objective_function(x):
    return -(x - 3)**2 + 9
def hill_climb():
    current_x = random.uniform(0, 6)
    current_value = objective_function(current_x)
    step_size = 0.1
    for _ in range(100):
        new_x = current_x + random.uniform(-step_size, step_size)
        new_value = objective_function(new_x)
        if new_value > current_value:
            current_x, current_value = new_x, new_value
    return current_x, current_value
best_x, best_value = hill_climb()
print(f"Best solution: x = {best_x:.3f}, f(x) = {best_value:.3f}")

#Q2
import tensorflow as tf
from tensorflow.keras import layers, models
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(3, activation='softmax') 
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

