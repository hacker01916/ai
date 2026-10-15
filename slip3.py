#Q1
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [9, 10],
    6: [11, 12],
    7: [13, 14, 15],
    8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []
}
print("BFS Traversal:")
bfs(graph, 1)


#Q2
import math
def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):
    if depth == maxDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 2, 9, 0, 7] 
print("Optimal value:", alphabeta(0, 0, True, values, -math.inf, math.inf, 3))


##Q2
p = True
q = False
print("P AND Q =", p and q)
print("P OR Q =", p or q)
print("NOT P =", not p)
print("NOT Q =", not q)
