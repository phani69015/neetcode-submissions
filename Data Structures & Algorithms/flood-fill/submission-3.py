from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc]==color:
            return image

        curr = image[sr][sc]
        q = deque()
        image[sr][sc]=color
        q.append((sr,sc))
        m = len(image)
        n = len(image[0])

        d = {
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        }

        while q:
            a = len(q)
            for _ in range(a):
                x,y = q.popleft()
                for i,j in d:
                    xi = x+i
                    yj = y+j
                    if 0<=xi<m and 0<=yj<n and image[xi][yj]==curr:
                        image[xi][yj]=color
                        q.append((xi,yj))
        return image



        