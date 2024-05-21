while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        break
    
    number = int(user_input)
    
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
