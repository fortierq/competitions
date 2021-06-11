use std::cmp;

impl Solution {
    pub fn stone_game_vii(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        let mut dp = vec![vec![0; n]; n]; // dp[i][j] will be the maximum gain for a player using stones[i..j]
        let mut s = vec![0; n+1];  // s[i] will be the sum of stones[..i]
        for i in 1..n+1 {
            s[i] = s[i-1] + stones[i-1];
        }
        for k in 1..n {
            for i in 0..n - k {
                dp[i][i+k] = cmp::max(-dp[i][i+k-1] + (s[i+k] - s[i]), -dp[i+1][i+k] + (s[i+k+1] - s[i+1]));
            }
        }
        return dp[0][n-1];
    }
}
