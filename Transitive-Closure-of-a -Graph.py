"""
Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph. 
Here reachable mean that there is a path from vertex i to j. The reach-ability matrix is called transitive closure of a graph.
"""


def trans(V, graph):
    # take all intersections as 0 first.
    t = [[0 for i in range(V)] for i in range(V)]
    
    # create a function to recursively call and change the value while doing dfs.
    def recur(curr, visited, row):
        t[row][curr] = 1
        visited[curr] = True
        for node in graph[curr]:
            if visited[node]== False:
                recur(node, visited, row)
    for i in range(V):
        visit = [False]*V
        recur(i, visit, i)
    return t
