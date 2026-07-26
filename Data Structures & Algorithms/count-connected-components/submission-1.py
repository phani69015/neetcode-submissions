class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #bfs
        # adj = [[]for _ in range(n)]

        # for x,y in edges:
        #     adj[x].append(y)
        #     adj[y].append(x)

        # vis = [False]*n
        # q = deque()
        # count = 0

        # for i in range(n):
        #     if not vis[i]:
        #         count+=1
        #         q.append(i)
        #         vis[i]=True

        #         while q:
        #             key = q.popleft()
        #             for nei in adj[key]:
        #                 if not vis[nei]:
        #                     q.append(nei)
        #                     vis[nei]=True
        # return count

        #dfs 

        adj = [[]for _ in range(n)]

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        ans = 0 

        v = [False for _ in range(n)]

        def dfs(node):
            v[node]=True
            for nei in adj[node]:
                if not v[nei]:
                    v[nei]=True
                    dfs(nei)

        for i in range(n):
            if not v[i]:
                ans+=1
                dfs(i)

        return ans
        

                


        