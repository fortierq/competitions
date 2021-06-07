func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func minCostClimbingStairs(cost []int) int {
    dp := make([]int, len(cost) + 1)
    dp[0] = 0
    dp[1] = 0
    for i := 2; i < len(dp); i++ {
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    }
    fmt.Println(dp)
    return dp[len(dp) - 1]
}
