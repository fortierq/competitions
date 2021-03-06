class Solution:
    def minimumLengthEncoding(self, words) -> int:
        keep = []
        for w1 in words:
            add = True
            for i, w2 in enumerate(keep):
                if w1.endswith(w2):
                    add = False
                    keep[i] = w1
                if w2.endswith(w1):
                    add = False
            if add:
                keep.append(w1)
        return sum(len(w) for w in keep)
