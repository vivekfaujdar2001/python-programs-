a = eval(input("Enter the number : "))

for i in range (2,a):
    if a % i == 0:
        print ("prime not ")
        break

else:
    print ("prime no.")
