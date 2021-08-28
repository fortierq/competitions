var findLength = function(A, B) {
    const rows = A.length
    const cols = B.length
    
    const dp = Array(rows + 1).fill().map(() => Array(cols).fill(0))
    let max = 0
    
    for (let i = 1; i <= rows; i++) {
        for (let j = 1; j <= cols; j++) {
            if (A[i - 1] === B[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1
                max = Math.max(max, dp[i][j])
            }
        }
    }
    
    return max
};
