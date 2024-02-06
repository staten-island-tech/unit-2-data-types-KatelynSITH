#Data types, Numbers 1,2,3,.etc
def add(x,y):
    print(x+y)
add(45,35)

#Strings "a,b,c"
def message(name):
    print(name)
message("meow")

#NUMBERS ARE COMPLETELY DIFFERENT FROM STRINGS DUE TO DIFFERENT SIGNALS
#STRINGS MUST HAVE QUOTATION MARKS, NORMAL NUMBER CANNOT

X="1"
int(X)
#This way you can change data types
add("35","45")

#booleans(yay)
x = 5

def check(x):
    if(x>6):
        print("is logged in")
    else:
        print("please login")
check(x)