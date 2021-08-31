from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = defaultdict(list)
INF = int(1e9)
dis = [INF] * (V+1)                             #한 노드에서 다른 노드까지의 모든 가중치를 무한대로 초기화

for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
print(graph)

def dijkstra(start) :
    queue = []
    heapq.heappush(queue, (0, start))
    #print('queue=', queue)
    dis[start] = 0                              #자기 자신으로의 가중치는 0

    while(queue) :
        dist, now = heapq.heappop((queue))      #최단경로 초깃값 설정
        #print('dist=', dist, 'now=', now, 'dis[now]=', dis[now])
        if dis[now] < dist :                    #새로운 경로가 최소 가중치를 가진다면 --> 업데이트한다
            continue

        for node in graph[now] :
            cost = dist + node[1]               #최단경로 업데이트(node[1] = 연결된 노드간의 가중치)


            if cost < dis[node[0]] :
                #print('cost=', cost, 'node[0]=', node[0], 'dis[node[0]]=', dis[node[0]])
                dis[node[0]] = cost             #전체 최단경로 업데이트
                heapq.heappush(queue, (cost, node[0]))
                #print('queue=', queue)
                #print(dis)

dijkstra(K)

for i in range(1, V+1) :
    if dis[i] == INF :
        print("INF")
    else :
        print(dis[i])

'''
(sample)
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''