class Solution:
    def minimumLengthEncoding(self, words) -> int:
        ans = 0
        for i, w1 in enumerate(words):
            keep = True
            for j, w2 in enumerate(words):
                if i != j and w2.endswith(w1):
                    keep = False
            if keep:
                ans += len(w1)