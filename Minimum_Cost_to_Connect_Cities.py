"""
There are n cities and there are roads in between some of the cities. Somehow all the roads are damaged simultaneously. 
We have to repair the roads to connect the cities again. There is a fixed cost to repair a particular road. Find out the 
minimum cost to connect all the cities by repairing roads. Input is in matrix(city) form, if city[i][j] = 0 then there is 
not any road between city i and city j, if city[i][j] = a > 0 then the cost to rebuild the path between city i and city j is 
a. Print out the minimum cost to connect all the cities.
It is sure that all the cities were connected before the roads were damaged.
"""


class Cities:
    
    def __init__(self, n):
        self.n = n
        self.graph = [[0 for i in range(self.n)] for k in range(self.n)]
        
    def addedges(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w
        
    def least(self, distance, check):
        mn = float("inf")
        index = 0
        for i in range(self.n):
            if mn > distance[i] and check[i] == False:
                mn = distance[i]
                index = i
                
        return index
 
    def mindist(self): 
        dist = [float("inf")]*self.n
        mst  = [False]*self.n
        dist[0] = 0
        res = []
        
        for i in range(self.n):
            u = self.least(dist, mst)
            mst[u] = True
            res.append(dist[u])
            for j in range(self.n):
                if self.graph[u][j] > 0 and mst[j] == False and dist[j] > self.graph[u][j]:
                    dist[j] = self.graph[u][j]
                    
        return sum(res)
        
