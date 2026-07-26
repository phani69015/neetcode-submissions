from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        vis = [False]*n
        adj = [[] for _ in range(n)]

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        q = deque()
        c=0

        for i in range(n):
            if not vis[i]:
                q.append((i,-1))
                vis[i]=True
                c+=1
                if c>1:
                    return False

                while q:
                    node,par = q.popleft()
                    for nei in adj[node]:
                        if not vis[nei]:
                            vis[nei]=True
                            q.append((nei,node))
                        elif (vis[nei] and nei!=par):
                                return False
            
        return True
            





        







        