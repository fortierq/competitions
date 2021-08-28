package main

import (
	"fmt"
)

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxResult(nums []int, k int) int {
	h := &IntHeap{}
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		dp[i] = dp[i-1] + nums[i]
		for j := 1; j < k; j++ {
			if nums[j] >= 0 {
				
			}
			dp[i] = max(dp[i], dp[j]+nums[i])
		}
	}
	return dp[len(dp)-1]
}

func main() {
	s := []int{1, -1, -2, 4, -7, 3}
	fmt.Println(maxResult(s, 2))
}
