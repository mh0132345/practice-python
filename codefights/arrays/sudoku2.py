def unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue 
        if num in s:
            return False
        s.add(num)
    return True
        
def sudoku2(grid):
    for line in grid:
        if not unique(line):
            return False
    
    for i in range(9):
        if not unique([line[i] for line in grid]):
            return False
        
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            if not unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
            
    return True
