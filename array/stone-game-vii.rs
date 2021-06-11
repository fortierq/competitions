use std::cmp;

impl Solution {
    pub fn stone_game_vii(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        let mut dp = vec![vec![0; n]; n]; // dp[i][i+k] is 
        let mut s = vec![vec![0; n]; n];
        for i in 0..n {
            s[i][i] = stones[i];
        }
        for k in 1..n {
            for i in 0..n - k {
                s[i][i+k] = s[i][i+k-1] + stones[i+k];
                if (n - 1 - k) % 2 == 0 {
                    dp[i][i+k] = cmp::max(dp[i][i+k-1] + s[i][i+k-1], dp[i+1][i+k] + s[i+1][i+k]);
                }
                else {
                    dp[i][i+k] = cmp::min(dp[i][i+k-1] - s[i][i+k-1], dp[i+1][i+k] - s[i+1][i+k]);
                }
            }
        }
        return dp[0][n-1];
    }
}
