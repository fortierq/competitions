class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s) - k + 1):
            m = s[i:i+k]
            if m not in seen:
                seen.add(m)
        return len(seen) == 2**k
 
