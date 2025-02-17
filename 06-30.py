INF = 1e9

class Line:
  def __init__(self, u, v, w):
    self.u = u
    self.v = v
    self.w = w

def BellmanFord(s):
  global graph, weight, n, m
  weight[s] = 0
  for i in range(n - 1):
    for line in graph:
      u, v, w = line.u, line.v, line.w
      if weight[u] != INF and weight[u] + w < weight[v]:
        weight[v] = weight[u] + w
  for line in graph:
    u, v, w = line.u, line.v, line.w
    if weight[u] + w < weight[v]:
      weight[v] = -INF


while True:
  n, m, q, s = map(int, input().split())
  if n == 0:
    break
  graph = []
  weight = [INF] * (n + 1)
  for _ in range(m):
    u, v, w = map(int, input().split())
    graph.append(Line(u, v, w))
  BellmanFord(s)
  for k in range(q):
    f = int(input())
    if weight[f] == INF:
      print('Impossible')
    elif weight[f] == -INF :
      print('-Infinity')
    else:
      print(weight[f])
  print()

# MPI Maelstrom
import queue
INF = 1e9

class Node:
  def __init__(self, j, x):
    self.j = int(j)
    self.x = int(x)``
  def __lt__(self, other):
    return self.x < other.x

def Dijkstra():
  global graph, time
  pq = queue.PriorityQueue()
  pq.put(Node(0, 0))
  while pq.empty() == False:
    top = pq.get()
    u = top.j
    w = top.x
    for neighbor in graph[u]:
      if w + neighbor.x < time[neighbor.j]:
        time[neighbor.j] = w + neighbor.x
        pq.put(Node(neighbor.j, time[neighbor.j]))


n = int(input())
graph = [[] for _ in range(n + 1)]
time = [INF] * n
for i in range(1, n):
  a = input().split()
  for j in range(i):
    if a[j] != 'x':
      graph[i].append(Node(j, a[j]))
      graph[j].append(Node(i, a[j]))
Dijkstra()
min_time = -INF
for i in range(n):
  min_time = max(time[i], min_time)
print(min_time)

# for i in range(n - 1):    # for i in range(1, n):
#   #a = list(map(int, input().split()))   # Error for 'x'
#   a = input().split()
#   for j in range(i + 1):  #   for j in range(i):
#     if a[j] != 'x':
#       graph.append((i + 1, j + 1, int(a[j])))
#       graph.append((j + 1, i + 1, int(a[j])))

# BellmanFord(0)

# max_dist = -INF
# for i in range(n):
#   max_dist = max(dist[i], max_dist)  

# Alice in Wonderland
INF = 1e9

class Triad:
  def __init__(self, i, j, w):
    self.i = i
    self.j = j
    self.w = w

def BellmanFord(s):
  global graph, dist, n
  dist[s] = 0
  for i in range(n):
    for path in graph:
      u, v, w = path.i, path.j, path.w
      if dist[u] != INF and dist[u] + w < dist[v]: # Thieu dk dist[u] != INF
        dist[v] = dist[u] + w
  for path in graph:
      u, v, w = path.i, path.j, path.w
      if dist[u] != INF and dist[u] + w < dist[v]:
        dist[v] = -INF 

tc = 1
while True: 
  n = int(input())
  if n == 0:
    break
  graph = []
  dd = []
  monuments = []
  
  for i in range(n):
    k = input().split()
    monuments.append(k.pop(0))
    for j in range(len(k)):
      w = int(k[j])
      if i == j and w > 0:
        w = 0
      if i != j and w == 0:     # Thieu dieu kien nay
        continue
      graph.append(Triad(i, j, w))
    
      '''if i == j:
        if int(k[j]) < 0:
          w = -INF
        else:
          w = 0
      else:
        w = int(k[j])
      '''

  for i in range(n):
    dist = [INF] * n # Dinh danh so tu 0 thi chi can khai bao mang n phan tu
    BellmanFord(i)
    dd.append(dist)

  q = int(input())
  print('Case #{}:'.format(tc))
  for i in range(q):
    u, v = map(int, input().split())
    if dd[u][v] <= -INF:
      print('NEGATIVE CYCLE')
    elif dd[u][v] == INF:
      ans = 'NOT REACHABLE'
      print('{}-{} {}'.format(monuments[u], monuments[v], ans))
    else:
      ans = dd[u][v]
      print('{}-{} {}'.format(monuments[u], monuments[v], ans))
  
  tc += 1