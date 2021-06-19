impl Solution {
    pub fn min_refuel_stops(target: i32, start_fuel: i32, stations: Vec<Vec<i32>>) -> i32 {
        let mut dp = vec![start_fuel; stations.len() + 1]; // dp[j] is the max distance with at most j refuels
        for (i, s) in stations.iter().enumerate() {
            for j in (0..=i).rev() {
                if dp[j] >= s[0] {
                    dp[j + 1] = std::cmp::max(dp[j + 1], dp[j] + s[1]);
                }
            }
        }
        for (i, &e) in dp.iter().enumerate() {
            if e >= target {
                return i as i32;    
            }
        }
        -1
    }
}
