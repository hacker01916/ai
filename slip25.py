'''Q1) 
Write the program to implement the AO* Algorithm'''
# AO* Algorithm in Python
class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
        self.status = {}
        self.solution_graph = {}

    def ao_star(self, node):
        print("Expanding Node:", node)
        if node not in self.graph:
            self.status[node] = 'Solved'
            return self.heuristic[node]
        min_cost = float('inf')
        best_child = None
        for child_set in self.graph[node]:
            cost = sum(self.heuristic[c] + self.graph[node][child_set][c] for c in child_set)
            if cost < min_cost:
                min_cost = cost
                best_child = child_set
        self.solution_graph[node] = best_child
        self.status[node] = 'Solved'
        return min_cost
graph = {
    'A': {('B','C'): {'B':2,'C':3}},
    'B': {('D','E'): {'D':2,'E':3}},
    'C': {('F',): {'F':5}, ('G',): {'G':6}},
    'D': {('H','I'): {'H':2,'I':3}},
    'E': {('J',): {'J':1}}
}
heuristic = {'A':7,'B':6,'C':4,'D':5,'E':3,'F':6,'G':5,'H':0,'I':0,'J':0}
g = Graph(graph, heuristic)
print("Cost from A:", g.ao_star('A'))



'''Q2 Write a program to implement the Minimax Algorithm for a two-player 
game. '''
def minimax(depth, node_index, is_max, scores, height):
    if depth == height:
        return scores[node_index]
    if is_max:
        return max(minimax(depth+1, node_index*2, False, scores, height),
                   minimax(depth+1, node_index*2+1, False, scores, height))
    else:
        return min(minimax(depth+1, node_index*2, True, scores, height),
                   minimax(depth+1, node_index*2+1, True, scores, height))
scores = [3,5,2,9]  # D,E,F,G
height = 2
print("Optimal value:", minimax(0, 0, True, scores, height))


'''Q2 (OR)Write a program to implement the Forward Chaining inference 
mechanism. '''

def forward_chaining(rules, facts, goal):
    while True:
        new_fact = None
        for rule in rules:
            if rule[0] in facts and rule[1] not in facts:
                facts.add(rule[1])
                new_fact = rule[1]
                print("Derived:", new_fact)
        if goal in facts or not new_fact:
            break
    return goal in facts
rules = [('A','B'), ('B','C'), ('C','D')]
facts = {'A'}
goal = 'D'
print("Goal achieved:", forward_chaining(rules, facts, goal))
