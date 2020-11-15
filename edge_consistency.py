# Spójność krawędziowa grafu
# Dla każdej krawędzi ustalamy przepustowość równą 1
# Dla dowolnego wierzchołka sprawdzamy przepływ do każdego z pozostałych
# i bierzemy miminum z przepływów.

import sys
import os
import copy
from dimacs import readSolution, loadDirectedWeightedGraph
from maxflow import maxflow


def convertToDictionary(V,L):
  graph = [ [] for _ in range(V)]
  g_map = {}
  for (x,y,c) in L:
    graph[x].append((y,c))
  for (x,y,c) in L:
    if (x,c) not in graph[y]:
      graph[y].append((x,1))
  for x in range(V):
    for (y,c) in graph[x]:
      g_map[(x,y)]=c
  return graph,g_map


def edge_c(V,L):
  s=1
  min_count = sys.maxsize
  G,G_map = convertToDictionary(V+1,L)
  for i in range(2,V+1):
    g=copy.deepcopy(G)
    g_map = copy.deepcopy(G_map)
    min_count=min(min_count, maxflow(g,g_map,s,i,V+1))

  return min_count

def run_edge_tests():
  directory = "graphs/connectivity"
  for filename in os.scandir(directory):
    if not filename.path.endswith(".py") and filename.is_file():
      (V,L) = loadDirectedWeightedGraph(filename)
      print(filename)
      ans = str(edge_c(V,L))
      solution = readSolution(filename)
      if ans == solution:
        print("Correct! ", ans)
      else:
        print("Wrong!", ans, solution)

