from dataclasses import dataclass, field


@dataclass
class Trie:
    childs: dict = field(default_factory=dict)
    id_word: int = -1

class WordFilter:
    trie = Trie()
    trie_inv = Trie()
    def __init__(self, words: List[str]):
        self.w = words
        
        for i, w in enumerate(words):
            for t, w_ in [(self.trie, w), (self.trie_inv, w[::-1])]:
                node = t
                for c in w_:
                    if c not in node.childs:
                        node.childs[c] = Trie()
                    node = node.childs[c]
                node.id_word = i

    def find(self, prefix, t):
        node = t
        for c in prefix:
            if c not in node.childs:
                return
            node = node.childs[c]

        def dfs(v):
            if v.id_word != -1:
                yield v.id_word
            for c in v.childs.values():
                yield from dfs(c)
        
        yield from dfs(node)
            
    def f(self, prefix: str, suffix: str) -> int:
        s1 = set(self.find(prefix, self.trie))
        s2 = set(self.find(suffix[::-1], self.trie_inv))
        s = s1 & s2
        if not s:
            return -1
        print(self.w[max(s)])
        return max(s)
