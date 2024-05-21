sample = input("type here: ")
def count():
    upper_count = len([alphabets for alphabets in sample if alphabets.isupper()])
    lower_count = len([alphabets for alphabets in sample if alphabets.islower()])
    print("Upper case characters:", upper_count)
    print("Lower case characters:", lower_count)

count()
