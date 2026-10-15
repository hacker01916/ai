#Q1
from heapq import heappush, heappop
goal_state = [[1, 2], [3, 0]]  
def heuristic(state):
    dist = 0
    for i in range(2):
        for j in range(2):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = divmod(val - 1, 2)
                dist += abs(goal_i - i) + abs(goal_j - j)
    return dist
def get_neighbors(state):
    neighbors = []
    i, j = next((r, c) for r in range(2) for c in range(2) if state[r][c] == 0)
    moves = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    for x, y in moves:
        if 0 <= x < 2 and 0 <= y < 2:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            neighbors.append(new_state)
    return neighbors
def a_star(start):
    pq = []
    heappush(pq, (heuristic(start), start, []))
    visited = set()
    while pq:
        _, state, path = heappop(pq)
        if state == goal_state:
            return path + [state]
        visited.add(str(state))
        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                heappush(pq, (len(path)+1+heuristic(neighbor), neighbor, path+[state]))
    return None
start_state = [[1, 0], [3, 2]]
solution = a_star(start_state)
for step in solution:
    print(step)


#Q2
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Minimax value:", minimax(0, 0, True, values, float('-inf'), float('inf')))



#Q2(OR)
rules = {
    "fever": "Take rest and drink fluids.",
    "cold": "Use nasal drops and stay warm.",
    "headache": "Take pain relief and relax."
}
symptom = input("Enter your symptom: ").lower()
print(rules.get(symptom, "Consult a doctor for proper diagnosis."))
