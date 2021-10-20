'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.'''

'''
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

import collections

# using DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input validation; make sure grid exists
        if not grid:
            return 0
        
        # get dimensions of grid; aka how many sublists within grid list and how many elements in sublist
        rows, cols = len(grid), len(grid[0])
        # track visited
        visited = set()
        islands = 0

        # create the bfs function to use below
        def dfs(r, c):
            q = collections.deque()
            # record the cell that's been visited as a tuple
            visited.add((r, c))
            # also add it to our q
            q.append((r, c))

            # while our q is not empty...
            while q:
                # expand our island using dfs 
                # NOTE if we change it to just .popleft() it will become bfs
                row, col = q.pop()
                # check the just popped position's adjacent cells(right,left,above,below)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                # for each of these directions,
                for drow, dcol in directions:
                    # check if inbounds, is a '1'(land), and also has not been visited
                    if ((row + drow) in range(rows) and 
                        (col + dcol) in range(cols) and
                        grid[row + drow][col + dcol] == '1' and
                        (row + drow, col + dcol) not in visited):
                        # if matches all the above conditions, add to our q
                        q.append((row + drow, col + dcol))
                        # also add to our visited so we dont visit again (*add since its a set not a list)
                        visited.add((row + drow, col + dcol)) 
                        # NOTE  r + drow and c + dcol seem to have been used pretty repetitively so it defintely can be cleaned up
                        # such as --> putting ( r, c = row + drow, col + dcol ) just under the if statement




        # iterate through each row and column
        for r in range(rows):
            for c in range(cols):
                # we dont have to do anything if current == '0'(water) but if '1'(island)...
                # (dont forget to double check whether we've already visited this island)
                if grid[r][c] == "1" and (r,c) not in visited:
                    # ...then we have traverse it and mark it visited
                    # run breadth first search on this cell
                    dfs(r, c)
                    # increment number of islands
                    islands += 1

        return islands                    
