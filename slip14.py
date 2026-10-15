#Q1
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
graph = {
    'V1': {'V2', 'V3', 'V5'},
    'V2': {'V1', 'V4'},
    'V3': {'V1', 'V6'},
    'V4': {'V2', 'V5'},
    'V5': {'V1', 'V4', 'V6'},
    'V6': {'V3', 'V5'}
}
print("BFS Traversal starting from V1:")
bfs(graph, 'V1')


#Q2

class Entity:
    def __init__(self, name):
        self.name = name
class Person(Entity):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name, "Student")
        self.course = course
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name, "Teacher")
        self.subject = subject
teacher = Teacher("Dr. Rao", "Computer Science")
student = Student("Aniket", "B.Sc. Computer Science")
print(f"{student.name} studies {student.course} under {teacher.name}, who teaches {teacher.subject}.")
