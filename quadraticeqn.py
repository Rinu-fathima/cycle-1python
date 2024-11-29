import math
print("To solve Quadratic Equation:ax^2+bx+c")
a=int(input("Enter the coefficient a:"))
b=int(input("Enter the coefficient b:"))
c=int(input("Enter the coefficient c:"))
discriminant=b**2-4*a*c
if discriminant>0:
        root1=(-b+math.sqrt(discriminant))/(2*a)
        root2=(-b-math.sqrt(discriminant))/(2*a)
        print(f"The equation has two real roots:{root1} and {root2}")
elif discriminant==0:
        root=-b/(2*a)
        print(f"The equation has one real root:{root}")
else:
        realpart=-b/(2*a)
        imaginarypart=math.sqrt(-discriminant)/(2*a)
        print(f"The equation has two complex roots:{realpart}+{imaginarypart}i and {realpart}={imaginarypart}i")

