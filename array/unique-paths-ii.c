int uniquePathsWithObstacles(int** obstacleGrid, int m, int* n_){
    int n = *n_;
    obstacleGrid[0][0] = 1 - obstacleGrid[0][0];
    for(int i=1; i < m; ++i)
        obstacleGrid[i][0] = (1 - obstacleGrid[i][0])*obstacleGrid[i - 1][0];
    for(int j=1; j < n; ++j)
        obstacleGrid[0][j] = (1 - obstacleGrid[0][j])*obstacleGrid[0][j - 1];
    for(int i=1; i < m; ++i)
        for(int j=1; j < n; ++j) {
            obstacleGrid[i][j] = (1 - obstacleGrid[i][j])*(obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]);
        }
    return obstacleGrid[m - 1][n - 1];
}
