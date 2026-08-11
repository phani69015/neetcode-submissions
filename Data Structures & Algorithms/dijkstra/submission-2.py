class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        heap = []
        adj = [[] for _ in range(n)]
        for x,y,z in edges:
            adj[x].append([y,z])

        d = {}
        for i in range(n):
            d[i]=float("inf")
        d[src] = 0
        heapq.heappush(heap,[0,src])

        while heap:
            dist = heap[0][0]
            node = heap[0][1]
            heapq.heappop(heap) 

            for nei,nd in adj[node]:
                if dist + nd < d[nei]:
                    d[nei]=dist+nd 
                    heapq.heappush(heap,[nd+dist , nei]) 

        for i,j in d.items():
            if j == float("inf"):
                d[i] = -1
        return d

