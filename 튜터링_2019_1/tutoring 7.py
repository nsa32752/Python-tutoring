import sys
# N = sys.stdin.readline().rstrip()
# for x in range(int(N)):
#     inp = sys.stdin.readline().rstrip()
#     a, b = inp.split(" ")
#     sum = int(a) + int(b)
#     print(sum)

# def findPath(maze,N,x,y,sum):
#     if(x>=N or y>=N or x<0 or y<0):
#         return 0
#     elif(maze[x][y] != 1):
#         return 0
#     maze[x][y] = 0
#     return 1 + (findPath(maze,N,x-1,y,sum) + findPath(maze,N,x,y+1,sum) + findPath(maze,N,x,y-1,sum) + findPath(maze,N,x+1,y,sum))
#
# N= int(input())
# square = []
# for x in range(N):
#     inp = sys.stdin.readline().rstrip()
#     square += [[]]
#     for k in inp:
#         square[-1] += [int(k)]
# res = []
# for l in range(N):
#     for y in range(N):
#         if(square[l][y] == 1):
#             res += [findPath(square,N,l,y,0)]
# res.sort()
# print(len(res))
# for k in res:
#     print(k)

def DFS(gph, num):
    visited = []

    return

def BFS(gph, num):
    return

N, M, V = map(int,input().split(" "))
gph = []
for x in range(M):
    #print(gph)
    X, Y = map(int,input().split(" "))
    if X not in gph:
