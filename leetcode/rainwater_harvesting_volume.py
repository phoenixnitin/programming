"""
Rainwater harvesting problem.
Find total volume that can be stored
"""

import heapq as heap
from typing import List

#  3 3 3 3 3
#  3 2 4 2 3
#  3 4 1 4 3
#  3 2 4 2 3
#  3 3 2 3 3
# Result = 7

class Solution:
    """
    Solution
    """
    def trap_rain_water(self, height_map: List[List[int]]) -> int:
        """
        Calculate volume of harvested rainwater
        """
        if len(height_map) == 0:
            return 0
        if len(height_map[0]) == 0:
            return 0

        N = len(height_map)
        M = len(height_map[0])

        yet_to_explore = []
        heap.heapify(yet_to_explore)

        visited = [[0 for _ in range(len(height_map[0]))] for _ in range(len(height_map))]

        volume = 0
        max_height = 0

        for j in range(len(height_map[0])):
            heap.heappush(yet_to_explore, (height_map[0][j], (0,j)))
            visited[0][j] = 1
            bottom = len(height_map) - 1
            heap.heappush(yet_to_explore, (height_map[bottom][j], (bottom,j)))
            visited[bottom][j] = 1

        for i in range(1, len(height_map)-1):
            heap.heappush(yet_to_explore, (height_map[i][0], (i,0)))
            visited[i][0] = 1
            right = len(height_map[0]) - 1
            heap.heappush(yet_to_explore, (height_map[i][right], (i,right)))
            visited[i][right] = 1

        while yet_to_explore:
            height, (i,j) = heap.heappop(yet_to_explore)
            if height > max_height:
                max_height = height

            index_i = i-1
            index_j = j
            if index_i >= 0 and visited[index_i][index_j] == 0:
                visited[index_i][index_j] = 1
                h = max_height - height_map[index_i][index_j]
                heap.heappush(yet_to_explore, (height_map[index_i][index_j], (index_i,index_j)))
                if h > 0:
                    volume += h

            index_i = i
            index_j = j + 1
            if index_j < M and visited[index_i][index_j] == 0:
                visited[index_i][index_j] = 1
                h = max_height - height_map[index_i][index_j]
                heap.heappush(yet_to_explore, (height_map[index_i][index_j], (index_i,index_j)))
                if h > 0:
                    volume += h

            index_i = i + 1
            index_j = j
            if index_i < N and visited[index_i][index_j] == 0:
                visited[index_i][index_j] = 1
                h = max_height - height_map[index_i][index_j]
                heap.heappush(yet_to_explore, (height_map[index_i][index_j], (index_i,index_j)))
                if h > 0:
                    volume += h

            index_i = i
            index_j = j - 1
            if index_j >= 0 and visited[index_i][index_j] == 0:
                visited[index_i][index_j] = 1
                h = max_height - height_map[index_i][index_j]
                heap.heappush(yet_to_explore, (height_map[index_i][index_j], (index_i,index_j)))
                if h > 0:
                    volume += h
        return volume

sol = Solution()

# print(sol.trap_rain_water([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
# Result = 4

# print(sol.trap_rain_water([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
# Result = 10

# print(sol.trap_rain_water([[3,3,3,3,3],[3,2,4,2,3],[3,4,1,4,3],[3,2,4,2,3],[3,3,2,3,3]]))
# Result = 7

inp = [
[14,17,18,16,14,16],
[17, 3,10, 2, 3, 8],
[11,10, 4, 7, 1, 7],
[13, 7, 2, 9, 8,10],
[13, 1, 3, 4, 8, 6],
[20, 3, 3, 9,10, 8]
]
print(sol.trap_rain_water(inp))
# Result = 25