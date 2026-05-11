import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dist_list = {}
        pq = []
        adj_list = {}

        for index in range(n):
            dist_list[index] = float("inf")
            adj_list[index] = []
        dist_list[src] = 0

        for u, v, w in edges:
            adj_list[u].append([v, w])
        
        heapq.heappush(pq, (src, dist_list[src]))
        while pq:
            node, distance = heapq.heappop(pq)
            if distance > dist_list[node]:
                continue
            for vertex, weight in adj_list[node]:
                check_dist = dist_list[node] + weight
                if check_dist < dist_list[vertex]:
                    dist_list[vertex] = check_dist
                    heapq.heappush(pq, (vertex, dist_list[vertex]))

        for key, value in dist_list.items():
            if value != float("inf"):
                continue
            else:
                dist_list[key] = -1
        return dist_list