text = "The computer is only a fast idiot. It has no imagination. It cannot originate action. It is, and will remain, only a tool of man."

count = {}


for x in text:
    if(x != ' ' and x != ',' and x != '.'):
        if(x in count):
            count[x] += 1
        elif(x not in count):
            count[x] = 1

print(list(count.keys()))

print(list(count.values()))


item = list(count.items())
item.sort()
for x in item:
    print(x[0],":", x[1])