import numpy as np
import networkx as nx
import csv
from collections import deque

FAR = 1e7

class logisticNetwork:
    def __init__(self):
        self.network = nx.Graph()
        self.f = open('graph.csv', 'r')
        self.data = csv.reader(self.f)
        next(self.data)
        for row in self.data:
            self.network.add_edge(row[0], row[1], weight=int(row[2]))

        self.hub_max = {'X': 1000, 'A': 700, 'B': 400, 'C': 550}

    def pathInfo(self, dep, arv):
        data = {}
        info = deque(nx.shortest_path(self.network, source=dep, target=arv, weight='weight'))
        info.popleft()
        Dis = 0
        data[dep] = 0
        arv = dep
        while len(info) > 1:
            dep = arv
            arv = info.popleft()
            dDis = nx.shortest_path_length(self.network, source = dep, target=arv, weight='weight')
            data[arv] = Dis + dDis
            Dis += dDis
        return data

    def hubSaturation(self):
        pass

    def sampleMaker(self, num):
        sample = list()
        for i in range(num):
            sample.append(np.random.choice(list(self.network.nodes), 2, False))
        return sample