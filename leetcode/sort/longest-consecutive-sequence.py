class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = dict()  # d[k] est le début de la suite consécutive finissant en k
        f = dict()  # f[k] est la fin de la suite consécutive commencant en k
        for n in nums:
            if n not in d:
                d[n] = n
                if n - 1 in d:
                    d[n] = d[n - 1]
                f[n] = n
                if n + 1 in f:
                    f[n] = f[n + 1]
                d[f[n]] = d[n]
                f[d[n]] = f[n]
                # print(f"d: {d}")
                # print(f"f: {f}")
        return max(f[k] - d[k] + 1 for k in d)
