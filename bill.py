bill = input("What was the cost of your bill? ")
service = ((input("How was the service today? ")))

if service == ("bad"):
    print(int(bill)*1)
elif service == ("okay"):
    print(int(bill)*1.15)
elif service == ("good"):
    print(int(bill)*1.20)
elif service == ("great"):
    print(int(bill)*1.25)
else:
    print("invalid response")

