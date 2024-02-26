x = (int(input("Please type the number for the gcf ")))
y = (int(input("Please type the second number for the gcf ")))
factor = []

def gcf(a,b):
    for i in range(x,y):
            if x%i == y%i:
                 factor.append(i):
                 print('GCF of', a, 'and', b, 'is', gcf(a,b))