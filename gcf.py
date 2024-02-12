x = (int(input("Please type the number for the gcf ")))
y = (int(input("Please type the second number for the gcf ")))

def gcf(x): 

    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
  
values = gcf(x)
print('Factoring next #')
values1 = gcf(y)

GCF_list = [values, values1] 
print(GCF_list)