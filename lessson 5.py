given_number = int(input("number: "))
def factorial(given_number):
    answer = range(1, given_number + 1)
    multiple = 1
    for num in answer:
        multiple *= num
    return multiple    
print("the factorial of ", given_number, "is", factorial(given_number))