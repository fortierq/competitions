class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans, cur, next = [root], []
        while cur:
            ans.append(sum(t.val for t in cur)/len(cur))
            for v in cur:
                for w in [v.left, v.right]:
                    if w:
                        next.append(w)
            cur, next = next[:], []
        return ans
