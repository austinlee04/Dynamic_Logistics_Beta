import numpy as np
import networkx as nx
import csv
from collections import deque

FAR = 1e7

#V400에서 딕셔너리 사용 --> V500에서는 허브 고유번호 붙이고 리스트 사용해 인덱스로 구분
class logisticNetwork:
    def __init__(self):
        self.network = nx.Graph()
        self.f1 = open('.csv', 'r')  # 도로망 정보
        self.f2 = open('.csv', 'r')  # 허브(연결정보, 처리용량 등) 정보
        self.road_data = csv.reader(self.f1)
        self.hub_data = csv.reader(self.f2)
        self.hub_max = list()

        for row in self.hub_data:
            self.network.add_edge(row[0], row[1], weight=int(row[2]))           # row 인덱스는 추후 변경
            self.hub_max.append()

        self.hub_queue = [[] for _ in range(len(self.hub_max))]

    def pathInfo(self, dep, arv):                       # 허브간 이동경로 정보
        data = {}
        info = deque(nx.shortest_path(self.network, source=dep, target=arv, weight='weight'))
        info.popleft()
        Dis = 0
        data[dep] = 0
        arv = dep
        while len(info) > 1:
            dep = arv
            arv = info.popleft()
            dDis = nx.shortest_path_length(self.network, source=dep, target=arv, weight='weight')
            data[arv] = Dis + dDis
            Dis += dDis
        return data

    def HUB_process(self):                                 # 허브 처리 대기열
        pass

    def HUB_Saturation(self):                               # 허브 포화도 계산
        saturation = [0 for _ in range(len(self.hub_max))]
        for i in range(len(self.hub_max)):
            saturation[i] = len(self.hub_queue[i]) / self.hub_max[i]

        return saturation

    def sampleMaker(self, num):                             # 샘플 생성 (무작위)
        sample = list()
        for i in range(num):
            sample.append(np.random.choice(list(self.network.nodes), 2, False))
        return sample

    def move(self):
        pass