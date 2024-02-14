a = (int(input("Please type the number for the gcf ")))
b = (int(input("Please type the second number for the gcf ")))

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        print("GCD of {a} and {b} is {gcd(a, b)}")