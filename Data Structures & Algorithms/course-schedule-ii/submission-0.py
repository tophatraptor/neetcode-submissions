class Node:
    def __init__(self, course_id):
        self.course_id = course_id
        self.parents = set()
        self.children = set()

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: Node(i) for i in range(numCourses)}
        for prereq in prerequisites:
            child, parent = prereq[0], prereq[1]
            courses[parent].children.add(child)
            courses[child].parents.add(parent)
        queue = deque()
        result = []
        while len(courses) > 0:
            for course in courses:
                course_node = courses[course]
                if len(course_node.parents) == 0:
                    queue.append(course)
            if len(queue) == 0:
                return []
            while len(queue) > 0:
                course = queue.popleft()
                node = courses[course]
                for child in node.children:
                    child_node = courses[child]
                    child_node.parents.remove(course)
                courses.pop(course)
                result.append(course)
        return result
            