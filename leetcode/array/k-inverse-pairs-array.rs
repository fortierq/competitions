impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut inv = vec![vec![0; k + 1]; n + 1];
        for i in 0..=n {
            inv[i][0] = 1;
        }
        for i in 1..=n {
            for j in 1..=k {
                for l in 0..=j {
                    if l < i {
                        inv[i][j] = (inv[i][j] + inv[i - 1][j - l]) % 1000000007;
                    }
                }
            }
        }
        inv[n][k]
    }
}
