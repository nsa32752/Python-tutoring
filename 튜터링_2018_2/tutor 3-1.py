def Check_len(password):
    if(len(password) >= 9):
        print("Password length is enough.")
        return 1
    else:
        print("Warning!!!!\t\t Password is too short.")
        return 0

def Check_upper_lower(password):
    isupper = 0
    islower = 0
    for x in password:
        if(x.isupper()):
            isupper += 1
        elif(x.islower()):
            islower += 1
    if(isupper == 0 or islower == 0):
        print("Warning!!!!\t\t Upper/Lower Case does not validate.")
        return 0
    else:
        print("Upper/Lower Case is satisfied.")
        return 1

def Check_digit(password):
    isdigit = 0
    for x in password:
        if(x.isdigit()):
            isdigit += 1
    if(isdigit == 0 or isdigit == len(password)):
        print("Warning!!!!\t\t Please input number and character.")
        return 0
    else:
        print("Character and number are mixed.")
        return 1

def level(num):
    if (num == 3):
        return "High"
    elif (num == 1):
        return "Low"
    elif (num == 2):
        return "Normal"
    elif (num == 0):
        return "Bad"

psword = str(input("Type your password: "))
print("Checking your password.....\n")
print("========== Checking Start ==========")
num = 0
num = int(Check_digit(psword)) + int(Check_len(psword)) + int(Check_upper_lower(psword))
print("========== Checking Done  ==========\n")

print("Your Password Level : {0:>10}".format(level(num)))

print("Your Password is \'",psword,"\'")


