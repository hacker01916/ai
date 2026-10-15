##Q1
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 6],
    5: [3, 6],
    6: [4, 5]
}
print("DFS Traversal starting from vertex 1:")
dfs(graph, 1)


#2'

facts = {
    "rainy": True,
    "have_umbrella": False
}
rules = [
    ("rainy and not have_umbrella", "Stay indoors"),
    ("rainy and have_umbrella", "Go outside with umbrella"),
    ("not rainy", "Enjoy outdoor activities")
]
def infer(facts, rules):
    for condition, action in rules:
        if eval(condition, {}, facts):
            print("Action:", action)

infer(facts, rules)


