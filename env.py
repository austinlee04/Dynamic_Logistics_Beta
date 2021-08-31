import numpy as np
import heapq

FAR = 1e6

class P2P_env():
    def __init__(self):
        self.edges = ['A', 'B', 'C', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M']
        self.Node_coordinate = {
            'X': [27, 32], 'A': [32, 36], 'B': [43, 19], 'C': [13, 23],
            'E': [60, 79], 'F': [69, 72], 'G': [79, 53], 'H': [43, 3],
            'I': [20, 9], 'J': [3, 8], 'K': [2, 34], 'L': [1, 55],
            'M': [9, 93]
        }
        self.graph = {
            'X':{'A', 'B', 'C'}, 'A':{'X', 'E', 'F', 'G'},
            'B':{'X', 'H', 'I', 'J'}, 'C':{'K', 'L', 'M'},
            'E':{'A'}, 'F':{'A'}, 'G':{'A'}, 'H':{'B'},
            'I':{'B'}, 'J':{'B'}, 'K':{'C'}, 'L':{'C'}, 'M':{'C'}
        }
        self.shortest_dis = {
            'X': {
                'X': 0, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'A': {
                'X': FAR, 'A': 0, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'B': {
                'X': FAR, 'A': FAR, 'B': 0, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'C': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': 0, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'E': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': 0,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'F': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': 0, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'G': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': 0, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'H': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': 0, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'I': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': 0, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'J': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': 0,
                'K': FAR, 'L': FAR, 'M': FAR
            },
            'K': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': 0, 'L': FAR, 'M': FAR
            },
            'L': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': 0, 'M': FAR
            },
            'M': {
                'X': FAR, 'A': FAR, 'B': FAR, 'C': FAR, 'E': FAR,
                'F': FAR, 'G': FAR, 'H': FAR, 'I': FAR, 'J': FAR,
                'K': FAR, 'L': FAR, 'M': 0
            },
        }

    def dijkstra(self, graph, start):
        queue = []
        heapq.heappush(queue, (0, start))
        while (queue):
            dist, now = heapq.heappop((queue))
            if now in self.graph[start]:
                newDis = self.find_dis(self.Node_coordinate(start), self.Node_coordinate(now))
            if newDis < dist :
                self.shortest_dis[start][now] = newDis
                continue

            for node in self.graph[now]:
                if self.shortest_dis[start][node] == FAR:
                    self.shortest_dis[start][node] = self.find_dis(self.Node_coordinate(start), self.Node_coordinate(node))
                cost = dist + self.shortest_dis[start][node]

                if cost < self.shortest_dis[start][node]:
                    self.shortest_dis[start][node] = cost
                    heapq.heappush(queue, (cost, node))

    def find_dis(self, P, Q):
        x = P[0] - Q[0]
        y = P[1] = Q[1]
        l = x**2 + y**2
        return np.sqrt(l)

    def sample_maker(self, num):
        sample = list()
        for i in range(num):
            sample.append(np.random.choice(self.edges, 2, False))
        return sample