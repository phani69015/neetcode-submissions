class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int frsh = 0;
        queue<pair<int, int>> q;
        for(int i = 0; i<n; i++){
            for(int j = 0; j<m; j++){
                if(grid[i][j] == 2){
                    q.push({i, j});
                }else{
                    if(grid[i][j] == 1){
                    frsh++;}
                }
            }
        }
        vector<pair<int, int>> d = {
            {-1,0},
            {1, 0},
            {0, 1},
            {0, -1},
        };
        int min = 0;
        while(!q.empty()){
            int size = q.size();
            for(int i = 0; i<size; i++){
            auto [x,y] = q.front();
            q.pop();
            for(auto [dx,dy] : d){
                int xi = x + dx;
                int yi = y + dy;
                if(xi>=0 && xi<n && yi>=0 && yi<m && grid[xi][yi] == 1){
                    grid[xi][yi] = 2;
                    q.push({xi, yi});
                    frsh -= 1;
                }
            }
            }
            if(!q.empty()){
                min+=1;
            }
        }
        if(frsh == 0){
            return min;
        }else{
            return -1;
        }
        
    }
};
