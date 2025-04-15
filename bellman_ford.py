import math


def bellman(graph,source):

    V = len(graph) # no of vertices
    dist = [math.inf]*V
    dist[source] = 0


    for _ in range (V+1):
        for u in range(V):
            for v in range(V):
                    if graph[u][v]!=math.inf:
                         if dist[u]+graph[u][v]<dist[v]:
                              dist[v]=graph[u][v]+dist[u]

    
    neg_edge = False
    for u in range(V):
         for v in range(V):
              if graph[u][v]!=math.inf:
                         if dist[u]+graph[u][v]<dist[v]:
                               neg_edge = True



    return dist,neg_edge

graph = [
    [0,     1,     4,     math.inf],
    [math.inf, 0,     4,     2],
    [math.inf, math.inf, 0,     3],
    [math.inf, math.inf, math.inf, 0]
]

distances, has_neg_cycle = bellman(graph, source=0)

print("Distances:", distances)
print("Negative Cycle Detected:", has_neg_cycle)