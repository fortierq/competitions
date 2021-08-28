class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        dist = [float("inf")]*n
        dist[0] = 0
        G = defaultdict(list)
        for u, v, t in roads:
            G[u].append((v, t))
            G[v].append((u, t))
            
        for _ in range(n):  # bellman-ford to compute distances
            for u, v, t in roads:
                if dist[u] + t < dist[v]:
                    dist[v] = dist[u] + t
                if dist[v] + t < dist[u]:
                    dist[u] = dist[v] + t
        
        n_paths = [0]*n
        n_paths[0] = 1                
        for d, u in sorted(zip(dist, range(n))):  # count paths
            for v, t in G[u]:
                if dist[v] == d + t:
                    n_paths[v] += n_paths[u]
                    
        return n_paths[-1] % (10**9 + 7)
