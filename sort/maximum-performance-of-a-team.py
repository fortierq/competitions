class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))
        engineers.sort(key=lambda e: -e[0])
        q = []
        maxi = 0
        sum_speed = 0
        for e, s in engineers:
            if len(q) == k:
                sum_speed -= heappop(q)
            sum_speed += s
            heappush(q, s)
            maxi = max(maxi, sum_speed*e)
        return maxi % (10**9 + 7)
