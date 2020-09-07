##base
for x in range(1,6,1):
    for y in range(x):
        print("*", end='')
    print()

print()
##1
for x in range(0,5,1):
    for k in range(x):
        print(" ", end='')
    for l in range(5-x,0,-1):
        print("*", end='')
    print()

##2
for x in range(5):
    for i in range(4-x):
        print(" ", end='')
    for j in range(2*x+1):
        print("*", end='')
    print()

##3

for x in range(7):
    for i in range(7):
        if x < 3:
            if( 3-x-1<i<3+x+1):
                print("*", end='')
            else:
                print(" ", end='')
        elif x == 3:
            print("*", end='')
        elif x > 3:
            if(3-(7-x) < i < 3+(7-x)):
                print("*", end='')
            else:
                print(" ", end='')
    print()

###4
for x in range(5):
    for i in range(5):
        if x == 0 or x == 4:
            print("*", end='')
        else:
            if i == 0 or i == 4:
                print("*", end='')
            else:
                print(" ", end='')
    print()