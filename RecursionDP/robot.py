"""
Problem: Imagine robot sitting on top left position on a grid. Move it all the way to bottom right position. You can only move right and down. 
Approach: Think about using top-down approach logic. How many ways can you get to last position (nth). Obviously, there's two ways. To get to position grid[row][col], you either have to be at position grid[row-1][col] (i.e if you are moving down) or at position grid[row][col-1](i.e if you are moving right). Thus, knowing this, we can work our way down until we get to [0][0]s position in the grid. We can doing it recursively.

"""

path=[]
def findPath(row, col, path):
#check out-of-bounds condition
    if row< 0 or col <0:
        return False
#if it's already at [0][0], it will be True else False
    isAtOrigin= (row==0) and (col==0)
#recursive part, every time you have two recurise call
    if isAtOrigin or findPath(row-1, col, path) or findPath(row, col-1, path):
        path.append((row, col))
        return True
    return False

print(findPath(2-1,2-1,path))
print(path)
#the runtime of the above code O(2^row+col). this is because every time you have 2 other recursive calls. 

#Dynamic Programming:we know that some coordinates will fail. it'd nice we we cache those coordinates so we don't repeat.
path=[]
failed=[]
def findPath(row, col, path, failed):

    if row< 0 or col <0:
        return False
    if (row, col) in failed: #if coordinates in failed cache return false
        return False
    isAtOrigin= (row==0) and (col==0)
    if isAtOrigin or findPath(row-1, col, path, failed) or findPath(row, col-1, path, failed):
        path.append((row, col))
        return True
    points=(row, col)
    failed.append(points) #caching failed coordinate
    return False

print(findPath(30-1,30-1,path, failed))
print(path)

#THe time complexity will now be O(col*row) because we hit each cell just once.
