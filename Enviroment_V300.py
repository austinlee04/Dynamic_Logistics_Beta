import numpy as np
import networkx as nx

FAR = 1e7

class P2P_env():
    def __init__(self):
        self.edge = ['A', 'B', 'C', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M']
        self.graph = {
            'X':{'A', 'C'}, 'A':{'X', 'B', 'E'},
            'B':{'X', 'A', 'H'}, 'C':{'X', 'I', 'J', 'K'},
            'E':{'A', 'F', 'M'}, 'F':{'E', 'G'}, 'G':{'F'},
            'H':{'B', 'I'}, 'I':{'C', 'H', 'J'}, 'J':{'C', 'I', 'K'},
            'K':{'C', 'J', 'L'}, 'L':{'K', 'M'}, 'M':{'L', 'E'}
        }
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
        self.hub_max = {'X': 1000, 'A': 700, 'B': 400,'C': 550}

    def dijkstra_path(self, start):

    def route_weight(self):

    def hub_saturation(self):


    def sample_maker(self, num):
        sample = list()
        for i in range(num):
            sample.append(np.random.choice(self.edges, 2, False))
        return sample