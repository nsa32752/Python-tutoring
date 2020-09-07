file = open("text.txt", "r")
file2 = open("result.txt", "w")

words = []
dic = {}

line = file.readlines()
print(line)

for word in line:
    words += word.split()
print(words)

for x in words:
    x = x.lower()
    #print(x)
    if x.isalpha():
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1

file2.write("----------------------------------\n")
file2.write("{0:<15} | {1:>15}\n".format("word", "count"))
file2.write("==================================\n")

items = list(dic.items())

def byFreq(pair):
    return pair[1]

items.sort(key = byFreq, reverse = True)

for num in range(len(items)):
    word, count = items[num]
    file2.write("{0:<15} | {1:>15}\n".format(word, count))

file2.close()
file.close()