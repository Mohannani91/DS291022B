
num1,num2=1,1
print("fibonacci sequence:",num1,num2,end=" ")
for i in range(1,50,7):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3, end=" ")
print()