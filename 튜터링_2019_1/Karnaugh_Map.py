def change_1(s):
    for x in range(len(s)):
        if s[x] == '0':
            kar[0][0] = 1
        elif s[x] == '1':
            kar[1][0] = 1
        elif s[x] == '2':
            kar[3][0] = 1
        elif s[x] == '3':
            kar[2][0] = 1
        elif s[x] == '4':
            kar[0][1] = 1
        elif s[x] == '5':
            kar[1][1] = 1
        elif s[x] == '6':
            kar[3][1] = 1
        elif s[x] == '7':
            kar[2][1] = 1
        elif s[x] == '8':
            kar[0][3] = 1
        elif s[x] == '9':
            kar[1][3] = 1
        elif s[x] == '10':
            kar[3][3] = 1
        elif s[x] == '11':
            kar[2][3] = 1
        elif s[x] == '12':
            kar[0][2] = 1
        elif s[x] == '13':
            kar[1][2] = 1
        elif s[x] == '14':
            kar[3][2] = 1
        elif s[x] == '15':
            kar[2][2] = 1


def find8stra(kar, ans):
    for x in range(3):
        eight = 0
        sumup = 0
        sumdown = 0
        for y in range(4):
            sumup += kar[x][y]
            sumdown += kar[x+1][y]
        if(sumup == 4 and x==0):
            sum = 0
            for l in range(4):
                sum += kar[3][l]
            if(sum == 4):
                eight = 1
                ans += "+D'"
                if(kar[1][0] == 1 and kar[2][0] == 1 and kar[2][3] == 1 and kar[1][3] == 1):
                    ans += "+B'"
                    kar[1][0] = -1
                    kar[2][0] = -1
                    kar[2][3] = -1
                    kar[1][3] = -1
                kar[x] = [-1,-1,-1,-1]
                kar[3] = [-1,-1,-1,-1]
        if(sumup == 4 and sumdown == 4):
            kar[x] = [-1,-1,-1,-1]
            kar[x+1] = [-1,-1,-1,-1]
            if(x == 0):
                ans += "+C'"
            elif(x == 1):
                ans += "+D"
            elif(x == 2):
                ans += "+C"
        elif(sumup == 4 and eight == 0):
            kar[x] = [-1, -1, -1, -1]
            if (x == 0):
                ans += "+C'D'"
            elif (x == 1):
                ans += "+C'D"
            elif (x == 2):
                ans += "+CD"
        elif(sumdown == 4 and x == 2):
            kar[x+1] = [-1, -1, -1, -1]
            ans += "+CD'"
    for x in range(3):
        sumup = 0
        sumdown = 0
        for y in range(4):
            sumup += kar[y][x]
            sumdown += kar[y][x+1]
        if ((sumup == -4 or sumup == 4 )and x == 0):
            sum = 0
            for l in range(4):
                sum += kar[l][3]
            if (sum == 4 or sum == 0 and kar[0][3]!=0 and kar[1][3]!=0 and kar[2][3]!=0 and kar[3][3]!=0):
                ans += "+B'"
                for i in range(4):
                    kar[i][0] = -1
        if((sumup == 4 or sumup == 0)and (sumdown == 0 or sumdown == 4)):
            if(kar[0][x] == 0 or kar[1][x] == 0 or kar[2][x] == 0 or kar[3][x] == 0):
                continue
            elif (kar[0][x+1] == 0 or kar[1][x+1] == 0 or kar[2][x+1] == 0 or kar[3][x+1] == 0):
                continue
            else:
                for i in range(4):
                    kar[i][x] = -1
                    kar[i][x + 1] = -1
                if (kar[0][x] == 0 or kar[1][x] == 0 or kar[2][x] == 0 or kar[3][x] == 0):
                    break
                elif (kar[0][x + 1] == 0 or kar[1][x + 1] == 0 or kar[2][x + 1] == 0 or kar[3][x + 1] == 0):
                    break
                elif (x == 0):
                    ans += "+A'"
                elif (x == 1):
                    ans += "+B"
                elif (x == 2):
                    ans += "+A"
        elif (sumup == 4 or sumup == 0):
            if(kar[0][x] != 0 and kar[1][x] != 0 and kar[2][x]!=0 and kar[3][x] != 0):
                for i in range(4):
                    kar[i][x] = -1
                if (x == 0):
                    ans += "+A'B'"
                elif (x == 1):
                    ans += "+AB'"
                elif (x == 2):
                    ans += "+AB"
        elif ((sumdown == -4 or sumdown == 4) and x == 2):
            if(kar[0][2] == -1 and kar[0][1] == -1 and kar[3][1] == -1 and kar[3][2] == -1):
                return ans
            for i in range(4):
                kar[i][x+1] = -1
            ans += "AB'"
    return ans

def find4square(kar, ans):
    for x in range(3):
        for y in range(3):
            if(y==0):
                if (kar[x][0] + kar[x][3] + kar[x + 1][0] + kar[x + 1][3] == 4 or kar[x][0] + kar[x][3] + kar[x + 1][
                    0] + kar[x + 1][3] == 0 or kar[x][0] + kar[x][3] + kar[x + 1][0] + kar[x + 1][3] == -2 or kar[x][
                    0] + kar[x][3] + kar[x + 1][0] + kar[x +1][3] == 2):
                    if(kar[x][0] != 0 and kar[x][3] != 0 and kar[x+1][0] and kar[x+1][3] != 0):
                        if (x == 0):
                            ans += "+B'C'"
                        elif (x == 1):
                            ans += "+B'D"
                        elif (x == 2):
                            ans += "+B'C"
                        kar[x][0] = -1
                        kar[x][3] = -1
                        kar[x + 1][0] = -1
                        kar[x + 1][3] = -1
            if(x == 0 and kar[x][y] + kar[x][y+1] + kar[x+1][y] + kar[x+1][y+1] == -4):
                if (kar[x + 2][y]+kar[x + 2][y + 1]+kar[x + 3][y]+kar[x + 3][y + 1] == 4):
                    ans += "+A'"
                    kar[x+2][y]=-1
                    kar[x+2][y+1]=-1
                    kar[x+3][y]=-1
                    kar[x+3][y+1]=-1
            elif((kar[x][y] or kar[x+1][y] or kar[x][y+1] or kar[x+1][y+1])
                 and kar[x][y] != 0 and kar[x+1][y] != 0 and kar[x][y+1] != 0 and kar[x+1][y+1] != 0):
                if(kar[x][y]+kar[x+1][y]+kar[x][y+1]+kar[x+1][y+1] == 4
                        or kar[x][y]+kar[x+1][y]+kar[x][y+1]+kar[x+1][y+1] == 2
                        or kar[x][y]+kar[x+1][y]+kar[x][y+1]+kar[x+1][y+1] == 0
                        or kar[x][y]+kar[x+1][y]+kar[x][y+1]+kar[x+1][y+1] == -2):
                    kar[x][y] = -1
                    kar[x+1][y] = -1
                    kar[x][y+1] = -1
                    kar[x+1][y+1] = -1
                    if (x == 0):
                        ans += "+C'"
                    elif (x == 1):
                        ans += "+D"
                    elif (x == 2):
                        ans += "+C"
                    if (y == 0):
                        ans += "A'"
                    elif (y == 1):
                        ans += "B"
                    elif (y == 2):
                        ans += "A"
                    if (kar[x + 1][y + 1] == -1 and kar[x + 1][y] == -1):
                        if (kar[3][y] == 1 and kar[3][y + 1] == 1):
                            kar[3][y] = -1
                            kar[3][y+1] = -1
                            ans += "+D'"
                            if (y == 0):
                                ans += "A'"
                            elif (y == 1):
                                ans += "B"
                            elif (y == 2):
                                ans += "A"
                else:
                    break
            elif(kar[0][y] == 1 and kar[0][y+1] == 1):
                if((kar[3][y] == 1 or kar[3][y] == -1) and (kar[3][y]==1 or kar[3][y] == -1)):
                    kar[0][y] = -1
                    kar[0][y+1] = -1
                    kar[3][y] = -1
                    kar[3][y+1] = -1
                    ans += "+D'"
                    if (y == 0):
                        ans += "A'"
                    elif (y == 1):
                        ans += "B"
                    elif (y == 2):
                        ans += "A"

    if(kar[0][0]+kar[0][3]+kar[3][0]+kar[3][3] == 4 or kar[0][0]+kar[0][3]+kar[3][0]+kar[3][3] == 0 or kar[0][0]+kar[0][3]+kar[3][0]+kar[3][3] == -2 or kar[0][0]+kar[0][3]+kar[3][0]+kar[3][3] == 2  ):
        if(kar[0][0]==0 or kar[0][3]==0 or kar[3][0]==0 or kar[3][3] == 0):
            return ans
        else:
            kar[0][0] = -1
            kar[0][3] = -1
            kar[3][0] = -1
            kar[3][3] = -1
            ans += "+B'D'"
    return ans

def find2rowstr(ans,y):
    if(y==0):
        ans+="A'"
    elif(y==1):
        ans += "B"
    elif(y==2):
        ans += "A"
    return ans

def find2colstr(ans,y):
    if(y==0):
        ans+="C'"
    elif(y==1):
        ans += "D"
    elif(y==2):
        ans += "C"
    return ans

def find2row(kar, ans, k):
    for x in range(4):
        for y in range(3):
            if (kar[x][y]+kar[x][y+1] == k and kar[x][y] == 1):
                if(x==0):
                    ans += "+C'D'"
                elif(x==1):
                    ans += "+C'D"
                elif(x==2):
                    ans += "+CD"
                else:
                    ans += "+CD'"
                ans = find2rowstr(ans, y)
                kar[x][y] = -1
                kar[x][y + 1] = -1
            if(y==0):
                if(kar[x][0] == 1 and kar[x][0] + kar[x][3] == k ):
                    ans += "+B'"
                    if (x == 0):
                        ans += "C'D'"
                    elif (x == 1):
                        ans += "C'D"
                    elif (x == 2):
                        ans += "CD"
                    else:
                        ans += "CD'"
                    kar[x][0] = -1
                    kar[x][3] = -1
    return ans


def find2col(kar, ans, k):
    for x in range(3):
        for y in range(4):
            if(kar[x][y] == 1 and kar[x][y] + kar[x+1][y] == k):
                if(y==0):
                    ans += "+A'B'"
                elif(y==1):
                    ans += "+A'B"
                elif(y==2):
                    ans += "+AB"
                else:
                    ans += "+AB'"
                if(x == 0 and kar[x+2][y] == -1 and kar[x+3][y] == -1):
                    continue
                elif(x == 2 and kar[x-2][y] == -1 and kar[x-2][y] == -1):
                    continue
                else:
                    ans =find2colstr(ans, x)
                kar[x][y] = -1
                kar[x+1][y] = -1
            if(x==0):
                if((kar[0][y] == 1 or kar[0][y] == -1) and kar[0][y] + kar[3][y] == k):
                    ans += "+D'"
                    if (y == 0):
                        ans += "A'B'"
                    elif (y == 1):
                        ans += "A'B"
                    elif (y == 2):
                        ans += "AB"
                    else:
                        ans += "AB'"
                    kar[0][y] = -1
                    kar[3][y] = -1
    return ans

def find1fin(kar, ans):
    karans = [["A'B'C'D'", "A'BC'D'", "ABC'D'", "AB'C'D"],
              ["A'B'C'D","A'BC'D","ABC'D","AB'C'D"],
              ["A'B'CD", "A'BCD", "ABCD", "AB'CD"],
              ["A'B'CD'","A'BCD'","ABCD'","AB'CD'"]]
    for x in range(4):
        for y in range(4):
            if(kar[x][y] == 1):
                ans += ("+" + karans[x][y])
                kar[x][y] = -1
    return ans

def except8(kar, ans):
    ans = find4square(kar, ans)
    ans = find2col(kar, ans, 2)
    ans = find2row(kar, ans, 2)
    ans = find2col(kar, ans, 0)
    ans = find2row(kar, ans, 0)
    ans = find1fin(kar, ans)
    return ans

def include8(kar, ans):
    ans = find8stra(kar, ans)
    ans = find4square(kar, ans)
    ans = find2col(kar, ans, 2)
    ans = find2row(kar, ans, 2)
    ans = find2col(kar, ans, 0)
    ans = find2row(kar, ans, 0)
    ans = find1fin(kar, ans)
    return ans

kar = [[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
ans1 = ""
ans2 = ""


s = str(input()).split(' ') # 0 1 2 5 6 7 => a'b'c' + a'cd' + a'bd
change_1(s)
allsum = 0
for x in range(4):
    for y in range(4):
        allsum += kar[x][y]
if(allsum == 16):
    print(1)
else:
    kar1 = kar
    ans1 = except8(kar1, ans1)
    change_1(s)
    kar2 = kar
    ans2 = include8(kar2, ans2)
    ans = ""
    ans1list = list(ans1.split("+"))
    ans2list = list(ans2.split("+"))
    ans1len = 0
    ans2len = 0
    for x in ans1list:
        ans1len += len(x)
    for x in ans2list:
        ans2len += len(x)
    if (len(ans1list) < len(ans2list)):
        ans = ans1
    elif (len(ans1list) == len(ans2list)):
        if (ans1len < ans2len):
            ans = ans1
        else:
            ans = ans2
    else:
        ans = ans2

    if (ans[0] == "+"):
        ans = ans[1:]
    else:
        ans = ans
    print(ans)