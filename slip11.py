#Q1
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", minimax(0, 0, True, values, float('-inf'), float('inf')))


#Q2
rules = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"]
}
facts = {"D", "E"}
def backward_chaining(goal):
    if goal in facts:
        return True
    if goal not in rules:
        return False
    for subgoal in rules[goal]:
        if not backward_chaining(subgoal):
            return False
    return True
goal = "A"
print("Goal achieved:", backward_chaining(goal))


