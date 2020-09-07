#####1
# list1 = ['C','A','M','B','R','I','D','G','E']
# inp = input()
# for x in inp:
#     if x not in list1:
#         print(x,end='')

######2
# string = input()
# list1 = []
# for x in range(len(string)):
#     list1 += [string[x:]]
# list1.sort()
# for x in list1:
#     print(x)

######3
n = int(input())
lis = [0]
stack = []
k = 1
lis += map(int,input().split())
i = 1
while(i<n+1):
    if(lis[i] == k):
        lis[i] = 0
        k+=1
        i+=1
    else:
        if(len(stack) != 0):
            if(stack[0] == k):
                stack.pop()
                k+=1
            else:
                stack.append(lis[i])
                i+=1
        else:
            stack.append(lis[i])
            i+=1
while(len(stack) != 0):
    if(stack[0] == k):
        stack.pop()
        k+=1
    else:
        print("Sad")
        break
if(k == n+1):
    print("Nice")

#
# 1 3 5 2 4
#
# 5 4 1 3 2
