# ###1
# string = input()
# string2 = ""
# for x in string:
#     string2 = x + string2
# print(string2)

###2
# txt = input()
# string = ''
# count = 0
# for x in txt:
#     if(x == '.'):
#         string += x
#         count += 1
#         print(string)
#         string = ''
#     else:
#         string += x
# print(count)
#
###3
N = int(input())
list = []
count = 0

for x in range(N):
    list += [int(input())]

for x in range(len(list)):
    for y in range(x+1,len(list)):
        if list[x] > list[y]:
            count += 1
        else:
            break

print(count)