#11650
#
# import operator
#
# inp = int(input())
# lis=[]
# for x in range(inp):
#     a, b= map(int,input().split())
#     lis.append([a,b])
#
# lis.sort(key = operator.itemgetter(1))
# lis.sort(key = operator.itemgetter(0))
#
# for adf in lis:
#     print(adf[0],adf[1])

###1620

# import sys
#
# dic = {}
# N, M = map(int, input().split())
# for i in range (N):
#     st = sys.stdin.readline().rstrip()
#     dic[st] = i+1
# listname =  list(dic.keys())
# for j in range(M):
#     inp = sys.stdin.readline().rstrip()
#     if inp not in dic:
#         print(listname[int(inp)-1])
#     else:
#         print(dic[inp])
#
# N = int(input())
# print(4*N)
#
#
# ###15904
# string = str(input())
# wordlen = 0
# res = 0
# for x in string:
#     if(x == 'U' and wordlen == 0):
#         res += 1
#         wordlen += 1
#     elif(x == 'C' and (wordlen == 1 or wordlen == 3)):
#         res += 1
#         wordlen += 1
#     elif(x == 'P' and wordlen == 2):
#         res += 1
#         wordlen += 1
#
# if(res == 4):
#     print("I love UCPC")
# else:
#     print("I hate UCPC")
