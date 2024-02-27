x = (int(input("Please type the smaller number here ")))
y = (int(input("Please type the larger number here ")))
factor = []

def gcf(x,y):
    for i in range(x,y):
            if x%i == 0 and y%i == 0:
                 factor.append(i)
gcf(x,y)
print('GCF of', x, 'and', y, 'is', factor[1])