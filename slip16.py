#Q1

def dls(graph, start, goal, limit):
    print(f"Starting DLS from {start} to {goal} with depth limit {limit}")
    return recursive_dls(start, goal, graph, limit)
def recursive_dls(node, goal, graph, limit):
    print(f"Visiting node: {node}, Remaining depth: {limit}")
    if node == goal:
        return True
    elif limit <= 0:
        return False
    else:
        for child in graph.get(node, []):
            if recursive_dls(child, goal, graph, limit - 1):
                return True
        return False
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}
start = 1
goal = 6
limit = 2
found = dls(graph, start, goal, limit)
if found:
    print("Goal found within depth limit!")
else:
    print("Goal not found within depth limit.")



#Q2

rules = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E", "F"]
}
facts = {"D", "E", "F"}
def backward_chain(goal):
    print(f"Trying to prove: {goal}")
    if goal in facts:
        print(f"{goal} is a known fact.")
        return True
    elif goal in rules:
        for subgoal in rules[goal]:
            if not backward_chain(subgoal):
                return False
        print(f"{goal} is proven by its subgoals.")
        return True
    else:
        print(f"No rule or fact found for {goal}.")
        return False
goal = "A"
if backward_chain(goal):
    print(f"Conclusion: {goal} is TRUE.")
else:
    print(f"Conclusion: {goal} cannot be proven.")
