a = (int(input("Please type the number for the gcf ")))
b = (int(input("Please type the second number for the gcf ")))

i = 1
if(a % i == 0 and b % i == 0):
    def gcf(a,b):
        if(gcf(a,b)):
            print('GCF of', a, 'and', b, 'is', gcf(a,b))