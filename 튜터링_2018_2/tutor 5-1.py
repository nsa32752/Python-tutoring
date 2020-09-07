#arr = [0,0,0,0,0,0,0,0,0,0]

#num = 11

#for x in range(1,num+1):
 #   while(x>=10):
  #      arr[x%10] += 1
   #     x //= 10
    #arr[x] += 1

#mul = 1
#arr1 = [0,0,0,0,0,0,0,0,0,0]

#for x in range(3):
#    mul *= int(input())

#while(mul>=10):
#    arr1[mul%10] += 1
#    mul //= 10

#rr1[mul] += 1

#for x in arr1:
#    print(x)


#print(arr)

dic = {}
for x in range(8):
    num = int(input())
    dic[x+1] = num

list = list(dic.values())

list.sort()

sum = 0
for x in range(7,2,-1):
    sum += list[x]
print(sum)

value = 7

list1 = ""

for x in range(8):
    if (dic[x+1] in list[3:]):
        list1 += str(x+1)
        list1 += " "
        value-=1

print(list1)

