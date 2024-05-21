import math 
import cmath
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
 
def discriminant():
    first = b**2 - 4 * a * c
    part = 2 * a
    if first == 0:
        num1 = (-b + 0) / part
        num2 = (-b - 0) / part
        print("x =",num2,"and x=",num1)
    elif first > 0:
        num3 = (math.sqrt(first))
        num4 = (-b + num3) / part
        num5 = (-b - num3) / part
        print("x =",num4," and x =",num5)
    elif first < 0:
        num6 = (cmath.sqrt(first))
        num7 = (-b + num6) / part
        num8 = (-b - num6) / part
        print("x =",num7,"and x =",num8 )
discriminant()

