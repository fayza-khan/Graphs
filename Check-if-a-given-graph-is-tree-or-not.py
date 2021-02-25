"""
Problem:

Write a function that returns true if a given undirected graph is tree and false otherwise. 
 
Approach:

An undirected graph is tree if it has following properties. 
1) There is no cycle. 
2) The graph is connected.

For an undirected graph we can either use BFS or DFS to detect above two properties.

-> How to detect cycle in an undirected graph? 
For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is already 
visited and u is not parent of v, then there is a cycle in graph. If we don’t find such an adjacent for any vertex, we say that 
there is no cycle (See Detect cycle in an undirected graph for more details).
-> How to check for connectivity? 
Since the graph is undirected, we can start BFS or DFS from any vertex and check if all vertices are reachable or not. 
If all vertices are reachable, then graph is connected, otherwise not.
 

"""
def cycle(node, vis, parent):
  # mark node as visited.
  vis[node] = True
  for nei in graph[node]:
    if cycle(nei, vis, node)==True:
      return True
    elif parent != nei:
      return True
  return False

def treeornot(graph, n):
  visit = [False]*n
  # checks whether cycle exist or not.
  if cycle(0, visit, -1) == True:
    return False
  # checks whether graph is connected or not.
  for i in range(n):
    if visit[i] == False:
      return False
  return True
