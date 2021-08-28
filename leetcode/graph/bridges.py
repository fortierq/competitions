class Solution:
    def criticalConnections(self, n, connections):
        g = defaultdict(list)
        for i, j in connections:
            g[i].append(j)
            g[j].append(i)
        seen = Counter()  # vus[v] == 1 si v est en cours de traitement, vus[v] == 2 si traitement terminé
        bridges = []
        
        def dfs(v, pred):
            seen[v] = 1
            back = set()
            for w in g[v]:
                if seen[w] == 1:
                    back.add(w)
                if seen[w] == 0:
                    back |= dfs(w, v)
            seen[v] = 2
            back.discard(v)
            if len(back) == 0 and pred:
                bridges.append([pred, v])
            return back
        dfs(0, None)
        return bridges
