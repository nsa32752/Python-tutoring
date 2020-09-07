###1
def grea():
    arr = []
    for x in range(3):
        arr += input()
    l = int(arr[0]) ## 왼발잡이
    r = int(arr[1]) ## 오른발 잡이
    a = int(arr[2]) ##양발잡이
    if l != r:
        if l < r:
            for x in range(1,a+1):
                if l != r:
                    l += 1
                    a -= 1
            return l * 2 + (a // 2) * 2
        elif l > r:
            for x in range(1,a+1):
                if l != r:
                    r += 1
                    a -= 1
            return r * 2 + (a // 2) * 2
    elif l == r:
        return l + r + (a // 2) * 2

print(grea())

##2

N = int(input())
pcnum = []
# for x in range(100):
#     pcnum += [0]
# print(pcnum)
people = 0
for x in range(N):
    num = input()
    if num in pcnum:
        people += 1
    else:
        pcnum += num
print(pcnum)
print(people)