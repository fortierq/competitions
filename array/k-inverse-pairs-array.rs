impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut inv : Vec<i32> = vec![0; (n+1)*(k+1)];
        for i in 0..=n {
            inv[i*(k+1)] = 1;
        }
        for i in 1..=n {
            for j in 1..=k {
                for l in 0..=j {
                    if l < i {
                        inv[i*(k+1) + j] = (inv[i*(k+1) + j] + inv[(i - 1)*(k+1) + j - l]) % 1000000007;
                    }
                }
            }
        }
        inv[n*(k+1) + k]
    }
}
