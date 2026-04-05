class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        This is a graph we need to check if there are cycles or not so we need to do
        topo sort, if there are cycles then its not possible to complete, but if there
        arent then its possible

        We first count how many dependencies each course has so that we can start with
        the ones with the no pre reqs otherwise its not possible to start. 

        We also keep track of which all course are needed before you can start any other
        course. Then as we start checking and removing course we reduce the dependencies, 
        moment a neighbor hits 0 means we can study that course. We just cintinue this
        we cant add anything anymore and then check how many course have we marked off
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        finished_courses = 0

        while queue:
            course = queue.popleft()
            finished_courses += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return finished_courses == numCourses