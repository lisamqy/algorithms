'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''


# very similar to 200. number of islands
# solution using dfs recursively 

class Solution;
    def maxAreaOfIsland(self, grid):
        # initialize our r(ow) and c(olumn)
        rows, cols = len(grid), len(grid[0])

        # write our dfs helper function; passing in the row and col as args
        def dfs(r, c):
            # check if is inbounds or is 1
            # long version: if r >= 0 and c >= 0 and r < len(grid) [*which we set as the variable rows above^] and col < len(grid[0]) and grid[r][c] == 1
            if 0<=r<rows and 0<=c<cols and grid[r][c] == 1:
                # reset our grid[r][c] so we don't revisit; aka turn the 1 into a 0 to effectively marked it as seen
                grid[r][c] = 0
                # if so, recursively call on all four directions -> top bottom right left 
                # and have it add any other result the dfs call returns(if it discovers other islands/1's it'll keep adding up)
                # don't forget to add 1 to the return statement since the cell area has to be at least 1
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            # if not in bounds
            else:
                return 0

        # initialize our area_islands here to start at 0
        area_islands = 0
        
        # for every row in the range of 0 to num of rows
        for r in range(rows):
            # for every col in the range of 0 to num of cols
            for c in range(cols):
                # get the max of current area and what the dfs returns
                area_islands = max(area_islands, dfs(r,c))
        return area_islands

# Time & Space: O(m*n) since we have to iterate through the entire grid