word = input("word: ")
def palendrome():
    answer = word[::-1]
    if answer == word:
        print("its a palendrome")
    else:
        print("it is not")
palendrome()
    