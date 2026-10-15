#Q1

def hill_climb(f, x_start, step_size, max_iterations):
    x = x_start
    for i in range(max_iterations):
        next_x = x + step_size
        if f(next_x) > f(x):
            x = next_x
        else:
            step_size = -step_size / 2  # reverse and reduce step
    return x, f(x)
def f(x):
    return -x**2 + 4*x
best_x, best_y = hill_climb(f, x_start=0, step_size=0.1, max_iterations=100)
print("Maximum at x =", best_x, "with value =", best_y)


#Q2

import itertools
colors = ['Red', 'Green', 'Blue']
nodes = ['A', 'B', 'C', 'D', 'E']
edges = [('A','B'), ('A','C'), ('B','D'), ('C','E'), ('D','E')]
def is_valid(assign):
    for (x, y) in edges:
        if assign[x] == assign[y]:
            return False
    return True
for combo in itertools.product(colors, repeat=len(nodes)):
    assign = dict(zip(nodes, combo))
    if is_valid(assign):
        print("Valid colouring:", assign)
        break


