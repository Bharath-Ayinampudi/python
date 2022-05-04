a,b=0,1
n=int(input("Enter the range of the fabinocci series:"))
print("The fabinocci series is:")
for i in range(0,n):
    c=a+b
    a=b
    b=c
    print(c)
