import numpy as np
import networkx as nx

FAR = 1e7

class P2P_env():
    def __init__(self, size):
        self.graph = {
            'X':{'A':6, 'B':21, 'C':17}, 'A':{'X':6, 'B':20, 'E':51},
            'B':{'X':21, 'A':20, 'H':16}, 'C':{'X':17, 'I':16, 'J':18, 'K':16},
            'E':{'A':51, 'F':11, 'M':53}, 'F':{'E':11, 'G':21}, 'G':{'F':21},
            'H':{'B':16, 'I':24}, 'I':{'C':16, 'H':24, 'J':17},
            'J':{'C':18, 'I':17, 'K':26}, 'K':{'C':16, 'J':26, 'L':21},
            'L':{'K':21, 'M':39}, 'M':{'L':39, 'E':53}
        }
        self.map = nx.Graph(self.graph)
        self.map.add_nodes = 0
        '''
        self.path = {
            'X': {
                'X': {[], 0}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'A': {
                'X': {[], FAR}, 'A': {[], 0}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'B': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], 0}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'C': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], 0}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'E': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], 0},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'F': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], 0}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'G': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], 0}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'H': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], 0}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'I': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], 0}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'J': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], 0},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'K': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], 0}, 'L': {[], FAR}, 'M': {[], FAR}
            },
            'L': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], 0}, 'M': {[], FAR}
            },
            'M': {
                'X': {[], FAR}, 'A': {[], FAR}, 'B': {[], FAR}, 'C': {[], FAR}, 'E': {[], FAR},
                'F': {[], FAR}, 'G': {[], FAR}, 'H': {[], FAR}, 'I': {[], FAR}, 'J': {[], FAR},
                'K': {[], FAR}, 'L': {[], FAR}, 'M': {[], 0}
            },
        }
        '''     #self_path
        self.hub_max = {'X': 1000, 'A': 700, 'B': 400,'C': 550}
        self.graph_size = 10


    def dijkstra_path(self, start):
        pass

    def route_weight(self):
        pass

    def hub_saturation(self):
        pass


    def sample_maker(self, num):
        sample = list()
        for i in range(num):
            sample.append(np.random.choice(self.edges, 2, False))
        return sample