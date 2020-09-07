######1
import datetime
start = datetime.datetime.now() ##코드 실행 전 시간
sum = 0
for x in range(1000):
    sum *= x
finish = datetime.datetime.now() ##코드 실행 후 시간
print(finish-start) ## 코드 실행 시간 = 코드 실행 후 시간 - 코드 실행 전 시간

#######2
## 열린괄호 = (
## 닫힌괄호 = )
## 열린괄호면 stack에 push한다. 닫힌 괄호일경우에는 stack의 top을 pop해준다.
## 닫힌괄호가 input으로 들어올 때, stack이 empty일 경우 "NO"를 출력해주고 함수를 종료한다.
## 모든 input이 확인 되었을 때, "YES"를 출력해주고 함수를 종료한다.
## 모든 input이 확인 되었을 때, stack이 empty가 아닌 경우 "NO"를 출력해주고 함수를 종료한다.
n = int(input())
for i in range(n):
    stack = []
    ans = 0
    parenthesis = input()
    for x in parenthesis:
        if (x == '('):
            stack.append(x)
        else:
            if (len(stack) == 0):
                ans = 1
                break
            else:
                stack.pop()
    if (len(stack) != 0):
        print("NO")
    elif (ans == 0):
        print("YES")
    else:
        print("NO")

########3
## Baha enter를 받았을 경우 ['Baha','enter']로 나누어 list에 저장한다. 즉. list는 이중리스트이다.
## 각 사람의 이름은 list[index][0]이고 각 사람의 출입 여부는 list[index][1]이다.
## leave일 경우 enter라고 기록되어있으면 list2에서 remove시켜준다.
## enter일 경우 list2에 이름을 넣어준다.
## 모든 출입 여부를 확인한 후, list2에 남아있는 이름을 print해준다.
N = int(input())
list = []
record = []
for x in range(N):
    string = input()
    list += [string.split(' ')]
for l in list:
    if(l[1] == 'enter'):
        record += [l[0]]
    elif(l[1] == 'leave'):
        if l[0] in record:
            record.remove(l[0])
for x in record:
    print(x)

