number_1 = int(input("first number: ")) 
number_2 = int(input("second number: "))
number_3 = int(input("third number: "))



if number_1 > number_2: 
    max_number = number_1
elif number_2 > number_1:
    max_number = number_2
    
if max_number > number_3: 
    final_answer = max_number
elif number_3 > max_number:
    final_answer = number_3
print(final_answer)