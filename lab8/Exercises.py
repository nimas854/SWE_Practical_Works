from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=None):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 
        if weight is not None:
            self.weights[(vertex1, vertex2)] = weight
            self.weights[(vertex2, vertex1)] = weight  

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def find_shortest_path_bfs(self, start_vertex, end_vertex):
        queue = deque([(start_vertex, [start_vertex])])
        visited = set()

        while queue:
            current_vertex, path = queue.popleft()
            visited.add(current_vertex)

            for neighbor in self.graph[current_vertex]:
                if neighbor == end_vertex:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)

        return None

    def detect_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, -1):
                    return True
        return False

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.graph[current_vertex]:
                weight = self.weights.get((current_vertex, neighbor), 1)
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def is_bipartite(self):
        color = {}
        for vertex in self.graph:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0
                while queue:
                    u = queue.popleft()
                    for neighbor in self.graph[u]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[u]
                            queue.append(neighbor)
                        elif color[neighbor] == color[u]:
                            return False
        return True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)


print("\nShortest path from 0 to 3 using BFS:")
print(g.find_shortest_path_bfs(0, 3))


print("\nCycle detection result:")
print(g.detect_cycle())


g.add_edge(0, 3, weight=5)
print("\nDijkstra's shortest path distances from vertex 0:")
print(g.dijkstra(0))


print("\nIs the graph bipartite?")
print(g.is_bipartite())
