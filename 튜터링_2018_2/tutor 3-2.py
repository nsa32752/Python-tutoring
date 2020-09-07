def FindMax(list):
    max = list[0]
    for x in list:
        if(max < x):
            max = x
    print("Max value is ", max)
    return max

def FindMin(list):
    min = list[0]
    for x in list:
        if (min > x):
            min = x
    print("Min value is ", min)
    return min

list = []

rot = ''

while(1):
    rot = input("How many number?(1~10): ")
    if(rot.isdigit() == True):
        rot = int(rot)
        if(0 < rot <= 10):
            for x in range(rot):
                num = int(input(str(x+1) + " : "))
                list += [num]
            break
        else:
            print("try again")
    elif (rot.isdigit() == False):
        if '-' in rot:
            print("try again")
        else:
            print("Just Number!!!")

print(list)

print("===== Find Max and Min value in the List =====")
max = FindMax(list)
min = FindMin(list)
print("Max_value - Min_value is ", max-min)
print("==============================================\n")

list.remove(max)
list.remove(min)

print("Average value of the List without max and min value")
sum = 0
for x in list:
    sum += x
print("Total sum is ", sum)
print("Length is ", rot -2)
print("Average value is ", sum/(rot-2))

