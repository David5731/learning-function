import math
number = float(input("num: "))
def perferct_square():
    square_root = (math.sqrt(number))
    square = square_root**2
    if square == number :
        print(number, "is a perfect square")
    else:
        print(number,"is not a perfect square")
perferct_square()