#Q1

from queue import PriorityQueue
def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    while not pq.empty():
        h, node = pq.get()
        if node in visited:
            continue
        print(node, end=" ")
        visited.add(node)
        if node == goal:
            print("\nGoal reached!")
            return
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3), ('E', 5)],
    'C': [('A', 4), ('F', 1)],
    'D': [('B', 3), ('F', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 1), ('D', 2), ('E', 1)]
}
heuristic = {'A': 6, 'B': 5, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
print("Best First Search Path:")
best_first_search(graph, 'A', 'F', heuristic)



#Q2
def AND(p, q):
    return p and q
def OR(p, q):
    return p or q
def IMPLIES(p, q):
    return (not p) or q
P = True
Q = False
R = True
expr1 = AND(P, OR(Q, R))          
expr2 = IMPLIES(P, Q)            
expr3 = OR(IMPLIES(Q, R), P)  
print("Expression 1 (P ∧ (Q v R)) =", expr1)
print("Expression 2 (P → Q) =", expr2)
print("Expression 3 ((Q → R) v P) =", expr3)
