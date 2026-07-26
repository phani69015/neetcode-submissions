class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        vis = [[0 for _ in range(n)]for _ in range(m)]

        d = {
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        }

        q = deque()
        comp = 0

        for u in range(m):
            for v in range(n):
                if vis[u][v]==0 and grid[u][v]=='1':
                    comp+=1
                    q.append((u,v))
                    vis[u][v]=1
                    while q:
                        x,y = q.popleft()
                        for i,j in d:
                            xi=x+i
                            yj = y+j
                            if 0<=xi<m and 0<=yj<n and vis[xi][yj]==0 and grid[xi][yj]=='1':
                                q.append((xi,yj))
                                vis[xi][yj]=1 
        return comp




        