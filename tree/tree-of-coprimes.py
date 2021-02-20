from math import gcd


def coprime(a, b):
    return gcd(a, b) == 1


class Solution:
    def getCoprimes(self, nums, edges):
        n = len(nums)
        fils = [[] for i in range(n)]
        res = [-1] * n

        cop = [[False for i in range(51)] for j in range(51)]  # store coprimes for efficiency
        for i in range(51):
            for j in range(51):
                cop[i][j] = coprime(i, j)
                
        def dfs(u, pere):
            if pere != -1:
                fils[pere].append(u)
            for e in edges:
                if u == e[0] and e[1] != pere:
                    dfs(e[1], u)
                if u == e[1] and e[0] != pere:
                    dfs(e[0], u)
        dfs(0, -1)  # fill fils

        dict_path = dict()  # dict_path[nums[u]] is (u, depth of u)

        def f(u, d):
            w_max, h_max = -1, -1
            for val in dict_path:  # find coprime ancestro of u
                w, h = dict_path[val]
                if cop[val][nums[u]] and h > h_max:
                    h_max = h
                    w_max = w
            res[u] = w_max
            
            tmp = None
            if nums[u] in dict_path:
                tmp = dict_path[nums[u]]
            dict_path[nums[u]] = u, d

            for v in fils[u]:
                f(v, d + 1)
            
            if tmp is None:  # restore dict_path
                del dict_path[nums[u]]
            else:
                dict_path[nums[u]] = tmp

        f(0, 0)  # fill res
        return res

S = Solution()
print(S.getCoprimes([2,3,3,2], [[0,1],[1,2],[1,3]]))
