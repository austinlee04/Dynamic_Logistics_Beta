import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
'''
dep = ['X', 'X', 'X', 'A', 'A', 'B', 'C', 'C', 'C', 'E', 'E', 'F', 'H', 'I', 'J', 'K', 'L']
arv = ['A', 'B', 'C', 'B', 'E', 'H', 'I', 'J', 'K', 'F', 'M', 'G', 'I', 'J', 'K', 'L', 'M']
dis = ['6','21','17','20','51','16','16','18','16','11','53','21','24','17','26','21','39']
data = pd.DataFrame({'p1':dep, 'p2':arv, 'len':dis})
G = nx.from_pandas_edgelist(data, 'dep', 'arv', create_using=nx.Graph())
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
'''
#print(start)
graph = {
            'X':{'A':6, 'B':21, 'C':17}, 'A':{'X':6, 'B':20, 'E':51},
            'B':{'X':21, 'A':20, 'H':16}, 'C':{'X':17, 'I':16, 'J':18, 'K':16},
            'E':{'A':51, 'F':11, 'M':53}, 'F':{'E':11, 'G':21}, 'G':{'F':21},
            'H':{'B':16, 'I':24}, 'I':{'C':16, 'H':24, 'J':17},
            'J':{'C':18, 'I':17, 'K':26}, 'K':{'C':16, 'J':26, 'L':21},
            'L':{'K':21, 'M':39}, 'M':{'L':39, 'E':53}
        }
G = nx.Graph(graph)
print(G.degree())
#nx.draw(G, with_labels=True)
#plt.show()
#print(G.adj())