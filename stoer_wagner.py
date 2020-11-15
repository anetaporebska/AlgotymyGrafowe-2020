# https://faliszew.github.io/algograf/lab3
# Aneta

from dimacs import loadWeightedGraph, readSolution
from queue import PriorityQueue
import sys
import os


def merge(G,a,b):
  
  for (u,w) in G[b].items():

    if u==a:
      pass
    elif u in G[a]:
      G[a][u]=G[a][u]+w
      G[u][a]=G[u][a]+w
    else:
      G[a][u]=w
      G[u][a]=w

    del G[u][b]
  G[b]={}


def minumumCutPhase(G,start):
  # ile wierzchołków w G
  n = len(G)
  a = start


  # Ponieważ potrzebujemy kolejki, która najpierw zwraca elementy 
  # o większym priorytecie a nie mniejszym, to należy sumę wag 
  # umieszczać ze znakiem ujemnym.
  Q = PriorityQueue()
  visited = [False]*n
  visited[a]=True
  values=[0]*n
  for (u,w) in G[a].items():
    values[u]-=w
    Q.put((-w,u))

  #print(values)
  
  s =0 #last
  t =0  #last but one
        
  while not Q.empty():
    q = Q.get()
    v = q[1]
    
    if visited[v]:
      continue
    t = s
    s = v

    visited[v]=True
    cut = -q[0]
    for (u,w) in G[v].items():
      values[u]-= w
      if not visited[u]:
        Q.put((values[u],u))


  return (s,t,cut)

def no_vertices(G):
  v=0
  for i in range(len(G)):
    if len(G[i])>0:
      v+=1
  return v

def solve(G):
  result = sys.maxsize
  v = no_vertices(G)
  while v>2:
    s,t,cut = minumumCutPhase(G,1)
    merge(G,s,t)
    v-=1
    result = min(result, cut)
  
  return result

    
def run_tests():
  directory = "graphs/"
  for filename in os.scandir(directory):
    if not filename.path.endswith(".py") and filename.is_file():
      (V,L) = loadWeightedGraph(filename)
      print(filename)
      G = [{} for i in range(V+1)]

      for u, v, c in L: G[u][v] = G[v][u] = c

      ans = str(solve(G))
      solution = readSolution(filename)
      if ans == solution:
        print("Correct! ", ans)
      else:
        print("Wrong!", ans, solution)


run_tests()
