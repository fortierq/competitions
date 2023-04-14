pub fn longest_palindrome_subseq(s: String) -> i32 {
    let n = s.len();
    let mut dp = vec![vec![0; n]; n];
    for i in 0..n {
        dp[i][i] = 1;
    }
    let b = s.as_bytes();
    for i in (0..n).rev() {
        for j in i+1..n {
            dp[i][j] =
                if b[i] == b[j] { dp[i+1][j-1] + 2 }
                else { dp[i+1][j].max(dp[i][j-1]) }
        }
    }
    dp[0][n-1]
}

fn main() {
    let s = String::from("cbbd");
    println!("{}", longest_palindrome_subseq(s));
}
