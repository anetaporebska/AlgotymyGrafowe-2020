import sys
import os
import queue
from dimacs import loadDirectedWeightedGraph, readSolution

def BFS(g,g_map,s,t,parent,V):
  visited = [False]*V
  q = queue.Queue()
  q.put(s)
  visited[s]=True

  while not q.empty():
    s = q.get() 
    for (v,c) in g[s]:
      if not visited[v] and g_map[(s,v)]>0:
        visited[v]=True
        q.put(v)
        parent[v]=s
        if visited[t]:
          return True
  
  return visited[t]
  
  

def maxflow(g,g_map,s,t,V):
  parent = [None]*V
  max_flow = 0

  while BFS(g,g_map,s,t,parent,V): # dopóki istnieje ścieżka powiększająca
    path_flow = sys.maxsize     # będę szukać minimalnej wagi krawędzi na ścieżce

    # przechodzę po ścieżce i szukam wagi ścieżki
    c = t
    while c!=s:https://github.com/anetaporebska/P-obiektowe-lab2/tree/lab5
      path_flow=min(path_flow, g_map[(parent[c],c)])
      c = parent[c]

    max_flow += path_flow

    # odejmuję path_flow od wagi wszystkich krawędzi po których przeszedł BFS
    # oraz dodaję path_flow do krawędzi wstecznej
    c = t

    while c!=s:
      x = parent[c]
      y = c
      g_map[(x,y)]=g_map[(x,y)]-path_flow
      if (y,x) in g:
        g_map[(y,x)]=g_map[(y,x)]+path_flow
      else:
        g_map[(y,x)]=path_flow
      c = parent[c]
    

  return max_flow


def convertToDictionary(V,L):
  graph = [ [] for _ in range(V)]
  g_map = {}
  for (x,y,c) in L:
    graph[x].append((y,c))
  for (x,y,c) in L:
    if (x,c) not in graph[y]:
      graph[y].append((x,0))
  for x in range(V):
    for (y,c) in graph[x]:
      g_map[(x,y)]=c
  return graph,g_map


def run_tests():
  directory = "graphs/flow"
  for filename in os.scandir(directory):
    if not filename.path.endswith(".py") and filename.is_file():
      (V,L) = loadDirectedWeightedGraph(filename)
      print(filename)
      g,g_map = convertToDictionary(V+1,L)
      ans = str(maxflow(g,g_map,1,V,V+1))
      solution = readSolution(filename)
      if ans == solution:
        print("Correct! ", ans)
      else:
        print("Wrong!", ans, solution)
