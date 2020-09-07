## 1
def fibonacci(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
for x in range(n):
    s = int(input())
    res = fibonacci(s)
    if(s != 0):
        one = fibonacci(s-1)
        zero = res-one
        print(zero, one)
    elif(s == 0):
        print(fibonacci(0), 0)

# ##2
#
# a = int(input())
# b = int(input())
# data = a**b
# while(data > 10):
#     data = data % 10
# print(data)
#
# ##3
#
# list = [[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
# sentence = input()
# ans = 0
# for x in sentence:
#     for y in range(10):
#         if x in list[y]:
#             ans += y
#
# print(ans)
#
# ##4
#
#
# def bsort(s):
#     for k in range(len(s)-1):
#         for i in range(len(s)-1):
#             if s[i] > s[i+1]:
#                 s[i], s[i+1] = s[i+1], s[i]
#     return s
#
# print(bsort([32,23,18,7,11,99,55]))
# print(bsort([12,4,6,1,31,223,16,17]))
# print(bsort([142,236,213,27,18,15]))
# print(bsort([17,5,1,3,21,45,26,7]))
# print(bsort([71,532,31,23,6,2,37,13]))