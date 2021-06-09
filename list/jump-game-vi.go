package main

import "fmt"

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func maxResult(nums []int, k int) int {
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		dp[i] = dp[i-1] + nums[i]
		for j := max(i-k+1, 0); j < i; j++ {
			dp[i] = max(dp[i], dp[j]+nums[i])
		}
	}
	return dp[len(dp)-1]
}

func main() {
	s := []int{1, -1, -2, 4, -7, 3}
	fmt.Println(maxResult(s, 2))
}
