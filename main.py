

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>b and a>c:
    Max = a
elif b>a and b>c:
    Max = b
else:
    Max = c
    
if a<b and a<c:
    Min = a
elif b<a and b<c:
    Min = b
else:
    Min = c

Mid = (a+b+c)-(Min+Max)

print("The numbers in ascending order: ",Min,Mid,Max)
