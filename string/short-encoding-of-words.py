
class Solution:
    def minimumLengthEncoding(self, words) -> int:
        trie = {}
        for w in words:
            node = trie
            for c in w[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            
        def dfs(node, depth):
            if not node:
                return depth + 1
            return sum(dfs(node[v], depth + 1) for v in node)
        return dfs(trie, 0)
