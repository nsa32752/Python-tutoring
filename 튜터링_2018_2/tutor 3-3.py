#1.
def fillwith_(sentence):
    new_sentence = ''
    for char in sentence:
        if char == ' ':
            char = '_'
        new_sentence += char
    return new_sentence

#print(fillwith_('아름다운 가을 단풍 구경하러 산으로 갑시다.'))

#2.
str = input()
num = 1
result = 0
for x in str:
    if(x=='O'):
        result += num
        num += 1
    elif(x=='X'):
        num = 1
print(result)

#3
def blast(ns):
    bs = []
    for x in ns:
        if x > 0:
            for i in range(x):
                bs += [x]
    return bs

#print(blast([]))
#print(blast([1,2,4]))
#print(blast([3,5]))
#print(blast([2,-3,3]))

#4
dic = {"A":'1', "B":'2', "C":'3', "D":'4', "E":'5', "F":'6'}
for x in dic:
    print(x + " : " + dic[x])


