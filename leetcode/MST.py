#1584. Min Cost to Connect All Points

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        cost = [float('inf')] * n
        cost[0] = 0
        ans = 0

        for _ in range(n):
            curr = -1

            # Find the unconnected point with minimum cost
            for i in range(n):
                if cost[i] != -1 and (curr == -1 or cost[i] < cost[curr]):
                    curr = i

            ans += cost[curr]
            cost[curr] = -1

            # Update costs using the newly connected point
            for i in range(n):
                if cost[i] != -1:
                    distance = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    cost[i] = min(cost[i], distance)

        return ans