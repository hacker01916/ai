#Q1
import random
def objective_function(x):
    return -(x - 3)**2 + 9  # peak at x = 3
def hill_climb():
    x = random.uniform(0, 10)
    step_size = 0.1
    for _ in range(100):
        new_x = x + random.choice([-step_size, step_size])
        if objective_function(new_x) > objective_function(x):
            x = new_x
    return x, objective_function(x)
best_x, best_y = hill_climb()
print("Best solution: x =", round(best_x, 2), "f(x) =", round(best_y, 2))




#Q2
facts = {"A"}
rules = {
    "A": "B",
    "B": "C",
    "C": "D"
}
def forward_chaining(facts, rules, goal):
    inferred = set(facts)
    while True:
        new_inferred = set()
        for premise, conclusion in rules.items():
            if premise in inferred and conclusion not in inferred:
                new_inferred.add(conclusion)
        if not new_inferred:
            break
        inferred.update(new_inferred)
        if goal in inferred:
            return True, inferred
    return False, inferred
goal = "D"
result, inferred = forward_chaining(facts, rules, goal)
print("Goal reached:", result)
print("Inferred facts:", inferred)

