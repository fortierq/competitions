# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, buy2, sell2 = np.inf, 0, np.inf, 0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p - buy1)
            buy2 = min(buy2, p - sell1)
            sell2 = max(sell2, p - buy2)
        return sell2