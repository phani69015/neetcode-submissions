class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [False for _ in range(m)] 
        q = deque()
        comp = 0

        for i in range(n):
            if not vis[i]:
                comp+=1
                q.append(i)
                vis[i]=True
                while q:
                    key = q.popleft()
                    for nei in range(len(grid[key])):
                        if not vis[nei] and grid[key][nei]==1:
                            q.append(nei)
                            vis[nei]=True
        return comp
                


