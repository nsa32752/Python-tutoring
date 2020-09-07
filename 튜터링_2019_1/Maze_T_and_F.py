# UNVISITED_WAY = 0
# WALL = 1
# BLOCKED = 3
# POSSIBLE_WAY = 2

def findPath(maze,x,y):
    if(x>7 or y>7 or x<0 or y<0):
        return False
    elif(maze[x][y] != 0): # 1, 2, 3 NOT UNVISITED WAY
        return False
    elif(x == 7 and y == 7):
        maze[x][y] = 2
        return True
    maze[x][y] = 2
    if(findPath(maze,x-1,y) or findPath(maze,x,y+1) or findPath(maze,x,y-1) or findPath(maze,x+1,y)):
        return True
    else:
        maze[x][y] = 3
        return False

maze1 = [[0,0,0,0,0,0,0,1],
         [0,1,1,0,1,1,0,1],
         [0,0,0,1,0,0,0,1],
         [0,1,0,0,1,1,0,0],
         [0,1,1,1,0,0,1,1],
         [0,1,0,0,0,1,0,1],
         [0,0,0,1,0,0,0,1],
         [0,1,1,1,0,1,0,0]]
print(findPath(maze1,0,0))

maze2 = [[0,1,0,0,0,0,0,1],
         [0,1,1,0,1,1,0,1],
         [0,0,0,1,0,0,0,1],
         [0,1,0,0,1,1,0,0],
         [0,1,1,1,0,0,1,1],
         [0,1,0,0,0,1,0,1],
         [0,0,0,1,0,0,0,1],
         [0,1,1,1,0,1,0,0]]
print(findPath(maze2,0,0))

maze3 = [[0,0,0,0,0,0,0,1],
         [1,1,1,0,1,1,0,1],
         [1,0,0,1,0,0,0,1],
         [1,1,0,0,1,1,0,0],
         [1,1,1,1,0,0,1,1],
         [0,1,0,0,0,1,0,1],
         [0,0,0,1,0,0,0,1],
         [0,1,1,1,0,1,0,0]]
print(findPath(maze3,0,0))

maze4 = [[0,0,0,0,0,0,0,1],
         [1,1,1,0,1,1,0,1],
         [1,0,0,0,0,0,1,1],
         [1,0,1,0,1,1,0,0],
         [1,0,0,1,0,0,0,1],
         [0,1,0,0,0,1,1,1],
         [0,0,0,1,1,1,0,1],
         [0,1,0,0,0,0,0,0]]
print(findPath(maze4,0,0))